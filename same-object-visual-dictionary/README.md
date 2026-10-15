# same-object-visual-dictionary

Python 3.10+, standard library only.
`python scripts/build_gallery.py manifest.json new-gallery-folder`
Manifest: {"anchor":"anchor.png","variants":[{"anchor":"anchor.png","image":"variant.png","prompt":"soft light","status":"GENERATED"}]}
Images must already exist within the manifest directory. This builds a gallery; it does not generate images or validate visual identity.

Published by miaorrr8888-cloud with AI-assisted development and cleanup. See the repository PROVENANCE.md and LICENSE.
Validation: run `python -m unittest discover -s tests -v` from the release root.
