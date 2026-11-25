# Public demonstration release policy

Publish only deliberately prepared public assets. Do not copy private project directories or runtime logs into this repository.

Permitted: synthetic inputs, scoped interface contracts, test specifications, redacted outputs, reproducibility instructions, measured outcomes, and explicitly approved public reference implementations.

Excluded: proprietary mechanisms, internal memory representations, private runtime or orchestration code, system prompts, secrets, credentials, customer or institutional identities and data, internal paths, unpublished research, and raw private conversations.

Commercial results require permission for publication and must distinguish a proposal, a signed engagement, delivery and measured outcome.

Before release:
- Verify that the artifact contains only deliberately approved public content.
- State whether the demonstration exercises a reference fixture or a real implementation through a bounded interface.
- Record acceptance criteria before testing and publish the observed outcome, including failures.
- Check all tracked files and commit history for accidental disclosure.
- Preserve the private implementation separately.
