# Kite Surf Tracker

First milestone: set up the tooling to grab the Kitesurf dataset from Roboflow Universe so you can start experimenting with models locally.

## Prerequisites
- Python 3.10+ recommended
- A (free) Roboflow account – needed to obtain an API key for dataset downloads

## Setup
1. (Optional) create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
2. Install required packages:
   ```powershell
   pip install -r requirements.txt
   ```
3. Generate or locate your Roboflow API key:
   - Log in at https://universe.roboflow.com/data-kitesurf/kitesurf-xthtz
   - Click **Download Dataset**
   - Copy the API key displayed in the download modal (or create one under **Settings → API Keys**)

## Downloading the dataset
The helper script downloads the dataset to `data/raw/` using the Roboflow Python SDK.

```powershell
$env:ROBOFLOW_API_KEY = "paste-your-key"
# Optional overrides:
# $env:ROBOFLOW_VERSION = "1"
# $env:ROBOFLOW_FORMAT = "yolov8"
# $env:ROBOFLOW_OUTPUT_DIR = "data/raw"
python scripts/download_dataset.py
```

When the download completes you should see the dataset extracted under `data/raw/kitesurf-xthtz-v1-yolov8/`.

If the dataset has more than one version, set `ROBOFLOW_VERSION` to the version number you want to pull. The default export format is `yolov8`; you can switch to other Roboflow-supported formats (e.g. `coco`, `pascal-voc`) with `ROBOFLOW_FORMAT`.

## Next steps
- Inspect the downloaded data (images, annotations) to confirm classes and annotation quality.
- Decide on preprocessing requirements before training (resize, augmentations, etc.).
