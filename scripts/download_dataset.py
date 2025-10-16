#!/usr/bin/env python3
"""
Download utility for the Kitesurf tracking dataset hosted on Roboflow Universe.

Usage:
    export ROBOFLOW_API_KEY="your_key"
    python scripts/download_dataset.py

Override the defaults when needed:
    ROBOFLOW_VERSION=1
    ROBOFLOW_FORMAT=yolov8
    ROBOFLOW_OUTPUT_DIR=data/raw
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from loguru import logger

try:
    from roboflow import Roboflow
except ImportError:  # pragma: no cover - defensive import guard
    logger.error(
        "Missing dependency: roboflow. Install it with `pip install -r requirements.txt`."
    )
    sys.exit(1)


WORKSPACE_SLUG = "data-kitesurf"
PROJECT_SLUG = "kitesurf-xthtz"


def read_env(name: str, default: str | None = None) -> str:
    """Fetch an environment variable or exit with a helpful message."""
    value = os.getenv(name, default)
    if value is None or value == "":
        logger.error("Environment variable {} is required.", name)
        sys.exit(1)
    return value


def main() -> None:
    api_key = read_env("ROBOFLOW_API_KEY")
    version = int(os.getenv("ROBOFLOW_VERSION", "1"))
    data_format = os.getenv("ROBOFLOW_FORMAT", "yolov8")
    output_root = Path(os.getenv("ROBOFLOW_OUTPUT_DIR", "data/raw"))

    destination = output_root / f"{PROJECT_SLUG}-v{version}-{data_format}"
    destination.parent.mkdir(parents=True, exist_ok=True)

    logger.info(
        "Downloading Roboflow dataset {}/{} (version {}) as `{}`...",
        WORKSPACE_SLUG,
        PROJECT_SLUG,
        version,
        data_format,
    )
    try:
        rf = Roboflow(api_key=api_key)
        project = rf.workspace(WORKSPACE_SLUG).project(PROJECT_SLUG)
        dataset = project.version(version).download(
            data_format,
            location=str(destination),
        )
    except Exception:  # pragma: no cover - surface helpful message
        logger.exception("Download failed")
        sys.exit(1)

    logger.info("Dataset saved to {}", dataset.location)


if __name__ == "__main__":
    main()
