# OPC Agent Legion Architecture

The root directory is the integration runtime. It exists so multiple standalone agent packages can be tested together under one Codex-recognized `.agents/` and `.codex/` structure.

## Three-Part Repository Model

```text
product/
  Finished outputs for marketplaces or direct sales.

no1 agent/
  Standalone package. Users copy the contents into a project root.

root runtime
  Integrated legion test area. Codex reads this directly.
```

## Integration Rule

Standalone packages should not be pasted into the root runtime unchanged. Integrated files must be namespaced.

```text
.agents/skills/no1-*
.agents/shared/no1/
.codex/agents/no1-*.toml
docs/no1/
examples/no1/
assets/no1/
```

When `no2` is ready, use the same pattern:

```text
.agents/skills/no2-*
.agents/shared/no2/
.codex/agents/no2-*.toml
docs/no2/
examples/no2/
assets/no2/
```

## Commander Layer

`.codex/agents/commander.toml` is the top-level router. It should know which subsystems exist and which orchestrator owns each domain.

The commander should not replace subsystem specialists. It should:

1. Classify the request.
2. Select the subsystem.
3. Select the specialist agent or skill.
4. Keep cross-subsystem work shallow and explicit.
5. Return a final synthesis only after specialist output is available.

## Files That Need Manual Integration

These files are not copied mechanically from standalone packages:

- Root `AGENTS.md`
- Root `README.md`
- Root `MANIFEST.md`
- `.codex/agents/commander.toml`
- `.codex/config.toml`
- shared `common/` files, if created later

These files define the combined runtime contract.
