#!/usr/bin/env python3
"""Stage gate checker for AI Native Founder Skill Pack.

Input JSON example:
{
  "stage": "idea",
  "evidence": {
    "target_user": "Finance managers at mid-market companies",
    "problem_specific": true,
    "frequency_defined": true,
    "severity_defined": true,
    "current_workaround": "spreadsheets and email",
    "real_conversations": 8,
    "solution_addresses_validated_problem": true,
    "disconfirming_evidence_reviewed": true
  }
}

The checker is intentionally conservative. Missing fields block passage.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

REQUIREMENTS = {
    "idea": [
        ("target_user", "Name the exact target user or persona."),
        ("problem_specific", "Problem must be specific, not a broad observation."),
        ("frequency_defined", "Frequency must be defined."),
        ("severity_defined", "Severity or cost must be defined."),
        ("current_workaround", "Current workaround or substitute must be named."),
        ("real_conversations", "Real user conversations must be completed."),
        ("solution_addresses_validated_problem", "Solution must address the validated problem."),
        ("disconfirming_evidence_reviewed", "Disconfirming evidence must be reviewed."),
    ],
    "mvp": [
        ("validated_problem", "Problem must be validated before MVP build."),
        ("mvp_scope", "MVP scope must define must-do and must-not-do."),
        ("architecture_context", "Architecture context must exist."),
        ("measurement_framework", "Activation, retention, revenue/referral metrics must be defined."),
        ("security_review_before_users", "Security review is required before real users."),
        ("feedback_loop", "Feedback collection and synthesis loop must exist."),
    ],
    "launch": [
        ("pmf_evidence", "Launch requires evidence of PMF, not only early traction."),
        ("repeatable_channel", "Growth must be channel-driven and repeatable."),
        ("unit_economics", "CAC/LTV/payback assumptions must be defensible."),
        ("production_readiness", "Infrastructure must handle production workloads."),
        ("security_compliance_review", "Security and compliance are no longer deferrable."),
        ("ops_without_founder_bottleneck", "Operations must run without founder as the single trigger."),
    ],
    "scale": [
        ("systematic_growth", "Growth must be systematic and auditable."),
        ("enterprise_readiness", "Documentation, support, SLAs, and observability must be enterprise-ready."),
        ("gtm_system", "GTM system must exist beyond founder-led selling."),
        ("governance_compliance", "Governance and compliance posture must withstand scrutiny."),
        ("founder_not_day_to_day_bottleneck", "Day-to-day operations must not depend on the founder."),
        ("moat_narrative", "The company must explain why users stay if an incumbent copies the product."),
    ],
}

NUMERIC_MINIMUMS = {
    "idea": {"real_conversations": 5},
}


def truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value > 0
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) > 0
    return False


def check_stage(stage: str, evidence: Dict[str, Any]) -> Dict[str, Any]:
    stage = stage.lower().strip()
    if stage not in REQUIREMENTS:
        return {
            "status": "ERROR",
            "stage": stage,
            "message": f"Unknown stage '{stage}'. Use one of: {', '.join(REQUIREMENTS)}.",
        }

    missing: List[Dict[str, str]] = []
    satisfied: List[str] = []
    warnings: List[str] = []

    for key, explanation in REQUIREMENTS[stage]:
        value = evidence.get(key)
        if not truthy(value):
            missing.append({"field": key, "reason": explanation})
        else:
            satisfied.append(key)

    for key, minimum in NUMERIC_MINIMUMS.get(stage, {}).items():
        value = evidence.get(key)
        if isinstance(value, (int, float)) and value < minimum:
            warnings.append(f"{key} is {value}; recommended minimum is {minimum}.")
            if not any(item["field"] == key for item in missing):
                missing.append({"field": key, "reason": f"Needs at least {minimum}."})

    status = "READY" if not missing else "NOT_READY"
    return {
        "status": status,
        "stage": stage,
        "satisfied": satisfied,
        "missing": missing,
        "warnings": warnings,
        "next_smallest_action": next_action(stage, missing),
    }


def next_action(stage: str, missing: List[Dict[str, str]]) -> str:
    if not missing:
        return "Proceed to the next stage only after reviewer checks for optimism and missing risks."
    field = missing[0]["field"]
    mapping = {
        "target_user": "Narrow the target user to a named persona and context.",
        "problem_specific": "Rewrite the problem as a testable hypothesis.",
        "real_conversations": "Run five customer discovery interviews with the target persona.",
        "mvp_scope": "Write the MVP scope: must-do, must-not-do, and evidence required to add features.",
        "architecture_context": "Create an architecture context document before any coding session.",
        "measurement_framework": "Define activation, D7, D30, revenue, referral, and false-positive metrics before launch.",
        "pmf_evidence": "Gather retention, revenue, referral, and qualitative pull evidence across multiple cycles.",
        "repeatable_channel": "Identify one acquisition channel with repeatable CAC/LTV/payback assumptions.",
        "production_readiness": "Run a launch readiness audit for infra, reliability, security, and observability.",
        "enterprise_readiness": "Create a gap analysis for docs, SLAs, support, incident response, and observability.",
        "gtm_system": "Build a GTM operating system beyond founder-led selling.",
        "moat_narrative": "Map domain depth, data flywheel, integrations, and workflow lock-in.",
    }
    return mapping.get(field, f"Fill missing evidence field: {field}.")


def print_markdown(result: Dict[str, Any]) -> None:
    print("\n## Stage Gate Check")
    print(f"Stage: {result.get('stage')}")
    print(f"Status: {result.get('status')}")
    if result.get("satisfied"):
        print("\nSatisfied:")
        for item in result["satisfied"]:
            print(f"- {item}")
    if result.get("missing"):
        print("\nMissing:")
        for item in result["missing"]:
            print(f"- {item['field']}: {item['reason']}")
    if result.get("warnings"):
        print("\nWarnings:")
        for item in result["warnings"]:
            print(f"- {item}")
    print(f"\nNext smallest action: {result.get('next_smallest_action')}")


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Check AI-native startup stage gate evidence.")
    parser.add_argument("input", type=Path, help="Path to evidence JSON.")
    parser.add_argument("--json-only", action="store_true", help="Print JSON only.")
    args = parser.parse_args(argv)

    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"Failed to read JSON: {exc}", file=sys.stderr)
        return 2

    stage = data.get("stage") or data.get("current_stage")
    evidence = data.get("evidence", data)
    if not stage:
        print("Input must include 'stage' or 'current_stage'.", file=sys.stderr)
        return 2

    result = check_stage(stage, evidence)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not args.json_only:
        print_markdown(result)
    return 0 if result.get("status") == "READY" else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
