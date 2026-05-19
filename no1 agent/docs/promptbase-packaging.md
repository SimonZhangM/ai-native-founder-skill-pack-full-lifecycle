# PromptBase Packaging

This document defines a practical sales package for PromptBase or similar
marketplaces. It is intentionally narrower than the public GitHub repository.

## Positioning

Recommended product name:

```text
AI Founder Stage Gate Skills Pack
```

Short positioning:

```text
A reusable SKILL.md workflow system that helps solo founders validate ideas,
scope MVPs, review PMF signals, and avoid building the wrong thing faster.
```

Use neutral wording:

- `Agent Skills Pack`
- `SKILL.md workflow system`
- `Codex-style agent workflows`
- `model-neutral`
- `not affiliated with OpenAI, Anthropic, Claude, or Codex`

Avoid wording that implies official status:

- `official Codex skills`
- `OpenAI certified`
- `Anthropic skills`
- `Claude official workflow`

## Recommended package

For PromptBase, ship a compact English-first ZIP:

```text
ai-founder-stage-gate-skills-pack/
  README.md
  INSTALL.md
  LICENSE.md
  DISCLAIMER.md
  .agents/
    skills/
  .codex/
    agents/
    config.toml
  shared/
    templates/
    references/
  examples/
    founder-intake-example.md
    idea-diagnosis-example.md
    mvp-scope-example.md
    pmf-review-example.md
```

If you want the simplest first SKU, omit scripts and ship instruction-only
skills. Add deterministic scripts in a later Pro version.

## Include

- `.agents/skills/` with all 9 `SKILL.md` workflows.
- `.codex/agents/` with all 6 agent definitions, if the package targets Codex
  users.
- A short install guide.
- A clear usage guide with 3-5 copyable prompts.
- 2-4 realistic example outputs.
- A disclaimer that the pack is independent and does not provide legal,
  financial, medical, or investment advice.
- A license that states whether buyers may use, edit, and reuse the pack across
  their own projects.

## Exclude from the sales ZIP

- `.git/`
- Local screenshots or generated images.
- Public-repo marketing files that are not needed by buyers.
- Bilingual duplicate docs unless the product explicitly promises both English
  and Chinese.
- Long design rationale docs.
- GitHub-specific maintenance files.
- Any references to being official, endorsed, certified, or affiliated.
- Shell history, local config, secrets, `.env`, or account-specific paths.

## Files to rewrite for a sales ZIP

Do not ship the public `README.md` unchanged. Create a buyer-facing README that
answers:

1. What problem this pack solves.
2. Who it is for and who it is not for.
3. What is included.
4. How to install it.
5. How to run the first stage diagnosis.
6. What outputs to expect.
7. What the pack cannot validate by itself.

Suggested disclaimer:

```text
This is an independent workflow pack. It is not affiliated with OpenAI,
Anthropic, Claude, Codex, or PromptBase. It does not replace real customer
research, professional advice, or founder judgment.
```

## Suggested first price

Start with:

```text
$9.99 - $14.99
```

The first goal is to validate whether buyers understand and install a
`SKILL.md` workflow pack. Consider a Pro version only after real buyer feedback.
