import csv


def load_csv(path):
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            lines = ["\t".join(row) for row in reader]
            return "\n".join(lines)
    except (OSError, csv.Error) as e:
        return f"Error loading CSV: {e}"


def utils_function():
    return None
