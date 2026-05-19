#!/usr/bin/env python3
"""Conservative PMF signal scorer.

Input JSON example:
{
  "activation_rate": 0.62,
  "day7_retention": 0.38,
  "day30_retention": 0.22,
  "paid_conversion": 0.11,
  "referral_rate": 0.08,
  "sean_ellis_very_disappointed": 0.43,
  "founder_intervention_level": "medium",
  "sample_size": 80
}
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def get_float(data: Dict[str, Any], key: str, default: float = 0.0) -> float:
    try:
        return float(data.get(key, default))
    except (TypeError, ValueError):
        return default


def score_pmf(data: Dict[str, Any]) -> Dict[str, Any]:
    activation = get_float(data, "activation_rate")
    d7 = get_float(data, "day7_retention")
    d30 = get_float(data, "day30_retention")
    paid = get_float(data, "paid_conversion")
    referral = get_float(data, "referral_rate")
    sean = get_float(data, "sean_ellis_very_disappointed")
    sample_size = int(get_float(data, "sample_size"))

    intervention = str(data.get("founder_intervention_level", "unknown")).lower()
    intervention_penalty = {
        "none": 0.0,
        "low": 0.03,
        "medium": 0.08,
        "high": 0.18,
        "heroic": 0.25,
        "unknown": 0.10,
    }.get(intervention, 0.10)

    score = (
        0.22 * clamp(activation / 0.7) +
        0.22 * clamp(d7 / 0.4) +
        0.24 * clamp(d30 / 0.25) +
        0.14 * clamp(paid / 0.12) +
        0.10 * clamp(referral / 0.10) +
        0.08 * clamp(sean / 0.40)
    ) - intervention_penalty

    score = round(clamp(score), 3)

    warnings: List[str] = []
    if sample_size < 30:
        warnings.append("Sample size is small; treat the score as directional only.")
    if activation > 0 and d7 == 0 and d30 == 0:
        warnings.append("Activation without retention can be a false positive.")
    if paid > 0 and d30 == 0:
        warnings.append("Revenue without retention can be a false positive.")
    if intervention in {"high", "heroic"}:
        warnings.append("High founder intervention means usage may be pushed rather than pulled.")
    if sean >= 0.40:
        warnings.append("Sean Ellis signal is positive, but no single metric confirms PMF.")

    if score >= 0.75 and d30 > 0 and intervention not in {"high", "heroic"}:
        band = "strong"
    elif score >= 0.55:
        band = "promising"
    elif score >= 0.35:
        band = "weak"
    else:
        band = "not_enough_signal"

    next_action = {
        "strong": "Run reviewer check for false positives, then prepare Launch readiness audit.",
        "promising": "Continue iteration and segment analysis before declaring PMF.",
        "weak": "Identify whether the gap is segment, positioning, onboarding, or product value.",
        "not_enough_signal": "Do not scale. Run customer discovery and MVP iteration diagnostics.",
    }[band]

    return {
        "pmf_signal_score": score,
        "band": band,
        "inputs": {
            "activation_rate": activation,
            "day7_retention": d7,
            "day30_retention": d30,
            "paid_conversion": paid,
            "referral_rate": referral,
            "sean_ellis_very_disappointed": sean,
            "founder_intervention_level": intervention,
            "sample_size": sample_size,
        },
        "warnings": warnings,
        "next_action": next_action,
    }


def print_markdown(result: Dict[str, Any]) -> None:
    print("\n## PMF Signal Score")
    print(f"Score: {result['pmf_signal_score']}")
    print(f"Band: {result['band']}")
    if result["warnings"]:
        print("\nWarnings:")
        for warning in result["warnings"]:
            print(f"- {warning}")
    print(f"\nNext action: {result['next_action']}")


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Score PMF signals conservatively.")
    parser.add_argument("input", type=Path, help="Path to PMF metrics JSON.")
    parser.add_argument("--json-only", action="store_true")
    args = parser.parse_args(argv)

    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"Failed to read JSON: {exc}", file=sys.stderr)
        return 2

    result = score_pmf(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not args.json_only:
        print_markdown(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
