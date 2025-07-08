"""
Configuration settings for the project
"""
import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Data processing settings
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
RANDOM_SEED = 42

# Visualization settings
FIGURE_SIZE = (12, 8)
DPI = 300

# API settings (if needed)
API_TIMEOUT = 30
MAX_RETRIES = 3
