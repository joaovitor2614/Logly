
from pathlib import Path
import os

dist_dir = os.path.join(Path(os.path.dirname(__file__)).parent, "web", "dist")
print('dist_dir', dist_dir)