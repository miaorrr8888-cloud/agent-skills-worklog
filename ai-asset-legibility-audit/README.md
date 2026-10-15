# ai-asset-legibility-audit

Python 3.10+, NumPy and Pillow (see requirements.txt).
Run `python references/legibility_audit.py --help`.
Invalid regions now raise an error; nonfinite scores are UNKNOWN.
Shape similarity is a heuristic; it does not certify text meaning or prove provenance.

Published by miaorrr8888-cloud with AI-assisted development and cleanup. See the repository PROVENANCE.md and LICENSE.
Validation: run `python -m unittest discover -s tests -v` from the release root.
