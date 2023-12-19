from __future__ import annotations

from pathlib import Path

import pytest


TEST_DIR = Path(__file__).parent.resolve()
FIXTURE_DIR = TEST_DIR / '_fixture_files'


@pytest.fixture
def get_list_response_sample() -> str:
    with open(FIXTURE_DIR / 'getListResponseSample.json') as f:
        return f.read()


@pytest.fixture
def get_details_response_sample() -> str:
    with open(FIXTURE_DIR / 'getDetailsResponseSample.json') as f:
        return f.read()
