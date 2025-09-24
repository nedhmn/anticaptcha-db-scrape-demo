import json
import os
from typing import Any

import httpx
from anticaptchaofficial.recaptchav3proxyless import (  # type: ignore
    recaptchaV3Proxyless,
)

from dbscrape.settings import settings
from dbscrape.utils import get_replay_id, validate_json_response

URLS = [
    "https://duelingbook.com/replay?id=72221622",
    "https://duelingbook.com/replay?id=72235918",
    "https://duelingbook.com/replay?id=72168747",
    "https://duelingbook.com/replay?id=72206688",
    "https://duelingbook.com/replay?id=72180020",
    "https://duelingbook.com/replay?id=72178434",
]


def main() -> None:
    for url in URLS:
        replay_id = get_replay_id(url)
        replay_json = scrape_url(url, replay_id)
        save_replay(replay_json, replay_id)


def save_replay(replay_json: dict[str, Any], replay_id: str) -> None:
    filename = f"data/replays/{replay_id}.json"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(replay_json, f)


def scrape_url(url: str, replay_id: str) -> dict[str, Any]:
    g_response = solve_recaptcha_v3(url)

    with httpx.Client() as client:
        data_url = f"https://www.duelingbook.com/view-replay?id={replay_id}"
        form_data = {"token": g_response, "recaptcha_version": 3, "master": False}
        response = client.post(url=data_url, data=form_data)

        return validate_json_response(response.json())


def solve_recaptcha_v3(url: str) -> str:
    solver = recaptchaV3Proxyless()
    solver.set_verbose(1)
    solver.set_key(settings.ANTICAPTCHA_API_KEY)
    solver.set_website_url(url)
    solver.set_website_key(settings.SITE_KEY)
    solver.set_min_score(0.9)

    g_response: str = solver.solve_and_return_solution()

    if g_response != "0":
        return g_response

    raise ValueError("Error with the CAPTCHA")


if __name__ == "__main__":
    main()
