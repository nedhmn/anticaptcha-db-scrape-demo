from typing import Any
from urllib.parse import parse_qs, urlparse


def get_replay_id(url: str) -> str:
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    replay_id = query_params.get("id")

    if replay_id is None:
        raise ValueError(f"No replay id found in URL: {url}")

    return replay_id[0]


def validate_json_response(response_data: Any) -> dict[str, Any]:
    if not isinstance(response_data, dict):
        raise ValueError("Response is not a dictionary")
    return response_data
