from __future__ import annotations

import logging
import os
import time
from pathlib import Path
from typing import Final, List
from dotenv import load_dotenv

load_dotenv()  # Load .env for local runs (no-op in CI when env vars already exist)

# --- Basic Setup --------------------------------------------------------------
README_FILE = Path("README.md")
# Index file to store all processed papers
INDEX_FILE = Path("web/public/arxiv.json")

# FIXME: Adding cs.LG/cs.AI can bring in many irrelevant papers (need stronger LLM filtering)
ARXIV_CATEGORIES: List[str] = ["cs.DC", "cs.OS"]

# Use OpenRouter (OpenAI-compatible); set API_KEY to your OpenRouter key
API_KEY = os.environ["API_KEY"]  # Use .get to avoid error if not set locally
BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "deepseek/deepseek-r1"

# --- Crawling Config ----------------------------------------------------------
# How many days back to look for delayed papers
LOOKBACK_DAYS = 7

# TODO: Subscribers (e-mail) ---------------------------------------------------
SUBSCRIBER: Final[dict[str, list[str]]] = {
    "zhixin@abc.com": ["thinking", "serving"],
    "test@tju.edu.cn": ["offloading", "RL"]
}


# --- Logging ------------------------------------------------------------------
class LOGGER:
    # fallback to print since logging will output too much information
    def debug(self, msg: str):
        print("[DEBUG] ({}): {}".format(time.strftime("%Y%m%d-%H%M%S", time.localtime()), msg))

    def info(self, msg: str):
        print("[INFO] ({}): {}".format(time.strftime("%Y%m%d-%H%M%S", time.localtime()), msg))

    def warning(self, msg: str):
        print("[WARNING] ({}): {}".format(time.strftime("%Y%m%d-%H%M%S", time.localtime()), msg))

    def error(self, msg: str):
        print("[ERROR] ({}): {}".format(time.strftime("%Y%m%d-%H%M%S", time.localtime()), msg))


logger = LOGGER()