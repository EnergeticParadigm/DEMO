# 01 — MCP execution authorization

Status: planned public evaluation; no executable harness or result has been released in this directory.

**Question:** Can an external agent attempt an unauthorized operation without that operation taking effect?

Use a synthetic, isolated target with no access to real files, accounts or production services. Define authorization and observable side effects before testing.

Minimum cases:
- Authorized action: permitted operation produces the expected state change.
- Unauthorized action: attempted operation is rejected and the target state remains unchanged.
- Changed authorization: a previously permitted operation is rejected after authorization is withdrawn.
- Verification: compare target state before and after each attempt; retain sanitized execution receipts.

A demonstration of a reference fixture does not establish enforcement by the private EP runtime. Any eventual EP-backed release must state its actual interface, tested scope and limitations. A superiority claim requires a matched strong conventional comparator.
