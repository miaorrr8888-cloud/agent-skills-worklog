# falsifiable-assertion-anchors

Python 3.10+, standard library only.
`python scripts/check_anchor.py --root <project> --anchor <anchor.json>`
Anchor JSON: file, original, rollback, command (an argv array). Run only trusted project tests.
The tool tests baseline, mutation and restoration in a temporary source copy.
A rollback must exit 1; other nonzero codes are not accepted as proof of an assertion failure.

Published by miaorrr8888-cloud with AI-assisted development and cleanup. See the repository PROVENANCE.md and LICENSE.
Validation: run `python -m unittest discover -s tests -v` from the release root.
