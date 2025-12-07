import os
import subprocess
from pathlib import Path
import importlib.util

# ------------------------
# Paths
# ------------------------
data_folder = Path("/app/data")
data_folder.mkdir(parents=True, exist_ok=True)

temp_leagues_folder = data_folder / "temp" / "leagues"
temp_leagues_folder.mkdir(parents=True, exist_ok=True)

json_file = data_folder / "tournaments_mzansi.json"
builder_file = data_folder / "league_builder.py"

# ------------------------
# Get Google Drive URLs from secrets
# ------------------------
json_url = os.environ.get("GDRIVE_JSON_URL")
builder_url = os.environ.get("GDRIVE_BUILDER_URL")
if not json_url or not builder_url:
    raise ValueError("Both GDRIVE_JSON_URL and GDRIVE_BUILDER_URL environment variables must be set!")

# ------------------------
# Download files with curl
# ------------------------
def download(url, output_path):
    print(f"Downloading {url} -> {output_path}")
    subprocess.run([
        "curl", "-L", "-o", str(output_path), url
    ], check=True)

download(json_url, json_file)
download(builder_url, builder_file)

# ------------------------
# Dynamically import the builder module
# ------------------------
spec = importlib.util.spec_from_file_location("league_builder", builder_file)
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

# ------------------------
# Run the generator
# ------------------------
builder.generate_leagues(
    json_path=json_file,
    output_folder=temp_leagues_folder
)
