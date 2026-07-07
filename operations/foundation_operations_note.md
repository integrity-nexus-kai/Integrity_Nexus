# Foundation Operations Routing Note

The Operations Layer describes practical execution structures that implement the Foundation Layer.

## Principle

```text
Operations implements Foundation.
Operations does not redefine Foundation.
```

## Scope

This layer may contain:

- workflow triggers,
- GitHub Actions checks,
- registry update procedures,
- review queue handling,
- agent prompts,
- issue/PR templates,
- audit exports,
- and execution protocols.

No operation may convert a candidate into canonical status without explicit review authorization.

This note links the new `foundation/` layer to future implementation work without forcing a full repository restructuring at this stage.
