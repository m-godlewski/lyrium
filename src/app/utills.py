import json


class FilesManager:
    """Class that contains methods used for files managing."""

    @staticmethod
    def load_json(path: str) -> dict:
        """Loads JSON file from given 'path', and returns file content as dictionary."""
        with open(path, "r") as f:
            return json.load(f)

    @staticmethod
    def save_json(path: str, data: dict):
        """Saves given dictionary as JSON file at given 'path'."""
        with open(path, "w") as f:
            json.dump(data, f)
