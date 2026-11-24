import os
import shutil

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile(os.path.join(os.path.dirname(__file__), "entry.png"),
                os.path.join(out_dir, "entry.png"))
print("entry.png written to", out_dir)
