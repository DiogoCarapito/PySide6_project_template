# pylint: disable=W0212

import csv
import sys
import os


def load_csv(path):
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            lines = ["\t".join(row) for row in reader]
            return "\n".join(lines)
    except (OSError, csv.Error) as e:
        return f"Error loading CSV: {e}"


def resource_path(rel_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, rel_path)
    return rel_path


def utils_function():
    return None
