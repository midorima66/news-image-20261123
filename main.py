"""Entry for the make.fun bounty news-image-20261123.

The image beside this file (entry.png) sums up the world news of Monday
23 November 2026. This program copies it to the output directory, the way
the kit's starter does: MAKEFUN_OUTPUT_DIR stands in for /output outside
the grader's container. No network, no inputs: every run writes the same
bytes.
"""

import os
import shutil
from pathlib import Path

src = Path(__file__).with_name("entry.png")
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out_dir / "entry.png")
