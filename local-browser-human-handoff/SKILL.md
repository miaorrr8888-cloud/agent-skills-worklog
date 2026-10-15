---
name: local-browser-human-handoff
description: Hand a browser login or CAPTCHA step to the user when automation cannot continue.
license: MIT
---

# Browser handoff

Use the available browser tool to open the exact requested page and verify it is visible.
Ask the user to complete login, MFA or CAPTCHA. Never read or export credentials or browser profiles.
After handoff, inspect the page again before claiming the workflow can continue.
An authenticated browser session does not prove another automation session is authenticated.
If the tool still cannot access results, request the relevant page content or a user-provided link.
Historical renderer crashes are environment-specific observations, not a ban on a browser or tool.
Do not disable sandbox, proxy or security settings as a workaround.
