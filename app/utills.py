import json
import os


class FilesManager:
    """Class that contains methods used for files managing."""

    @staticmethod
    def load_json(path: str) -> dict:
        """Loads JSON file from given 'path', and returns file content as dictionary."""
        if os.path.isfile(path):
            with open(path, "r") as f:
                return json.load(f)
        else:
            return {}

    @staticmethod
    def save_json(path: str, data: dict):
        """Saves given dictionary as JSON file at given 'path'."""
        with open(path, "w") as f:
            json.dump(data, f)


class POSMapper:
    """Class that is representation of POS tags mapper."""

    @staticmethod
    def map_pos_(tag: str) -> str:
        """Returns longer name of given POS tag."""
        pos_tag_map = {
            "ADJ": "ADJECTIVE",
            "ADP": "ADPOSITION",
            "ADV": "ADVERB",
            "CONJ": "CONJUNCTION",
            "DET": "DETERMINER",
            "NOUN": "NOUN",
            "NUM": "NUMERAL",
            "PRT": "PARTICLE",
            "PRON": "PRONOUN",
            "VERB": "VERB", 
            "X": "OTHER"
        }
        return pos_tag_map.get(tag, "UNDEFINED")
