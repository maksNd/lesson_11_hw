import json
from constants import JSON_FILE


def load_candidates(json_filepath: str = JSON_FILE) -> list[dict]:
    """Load data from json file"""
    with open(json_filepath, encoding='utf-8') as file:
        return json.load(file)


def get_candidate_by_id(candidate_id) -> dict:
    """Return candidate by id"""
    list_with_candidates = load_candidates()
    for candidate in list_with_candidates:
        if candidate_id == candidate['id']:
            return candidate


def get_candidates_by_quality(quality: str, field_to_find: str) -> list[dict]:
    """
    Return candidate by some quality.
    For example quality could be the name or the skill of the candidate.
    """
    list_with_candidates = load_candidates()
    list_with_wanted_candidates = []
    for candidate in list_with_candidates:
        if quality.lower().strip() in candidate[field_to_find].lower():
            list_with_wanted_candidates.append(candidate)
    return list_with_wanted_candidates
