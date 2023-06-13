import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Any
import json
import pandas as pd


def log_setting(
    log_folder: str = "logs-default", log_level: int = logging.INFO, stream: bool = True
) -> None:
    log_folder = log_folder if log_folder.startswith("logs-") else "logs-" + log_folder
    log_filename = os.path.join(
        Path(__file__).resolve().parents[1],
        log_folder,
        f"{datetime.now().strftime('%Y-%m-%d-%H:%M:%S')}.log",
    )
    Path(log_filename).parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_filename,
        level=log_level,
        format="[%(asctime)s] [%(name)s | line:%(lineno)s | %(funcName)s] [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    if stream:
        console = logging.StreamHandler()
        console_format = logging.Formatter("[%(name)s] [%(levelname)s] - %(message)s")
        console.setFormatter(console_format)
        logging.getLogger().addHandler(console)


def check_input_valid(x: str):
    try:
        assert str(abs(int(x.split(",")[0]))).isdigit()
    except Exception as e:
        return False
    return True


def read_data(path: str) -> Any:
    if path.endswith(".json"):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    elif path.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
        data = data.split("\n")
    elif path.endswith(".csv"):
        data = pd.read_csv(path)
    elif path.endswith(".ndjson"):
        data = pd.read_json(path, lines=True, orient="records")
    elif path.endswith(".ndjson.gz"):
        data = pd.read_json(path, lines=True, orient="records", compression="gzip")
    elif path.endswith(".pickle"):
        data = pd.read_pickle(path)
    elif path.endswith("parquet"):
        data = pd.read_parquet(path)
    else:
        data = []
    return data
