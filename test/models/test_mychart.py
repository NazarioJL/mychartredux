from __future__ import annotations

import json

from src.mychartredux.models.mychart import GetDetailsResponse
from src.mychartredux.models.mychart import GetListResponse
from src.mychartredux.models.mychart import ReferenceRange


def test_reference_range() -> None:
    results_range = """\
    {
        "low": 0.0,
        "high": 200.0,
        "displayLow": "0",
        "displayHigh": "200",
        "formattedReferenceRange": "0 - 200"
    }
    """

    reference_range = ReferenceRange.model_validate(
        json.loads(results_range, strict=False),
    )

    assert reference_range.low == 0.0
    assert reference_range.high == 200.0
    assert reference_range.display_low == '0'


def test_get_list_response(get_list_response_sample: str) -> None:
    get_list_response = GetListResponse.model_validate(
        json.loads(get_list_response_sample, strict=False),
    )
    assert len(get_list_response.new_result_groups) > 0


def test_get_details_response(get_details_response_sample: str) -> None:
    get_details_response = GetDetailsResponse.model_validate(
        json.loads(get_details_response_sample, strict=False),
    )
    assert len(get_details_response.results) > 0
