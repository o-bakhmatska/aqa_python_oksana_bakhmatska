import pytest
import requests

from .config import CARS_ENDPOINT, TOTAL_CARS_IN_DB
from .logger import LOGGER
from .functions import assert_sorted


class TestCarsSearch:

    @pytest.mark.parametrize(
        "sort_by,limit",
        [
            ("price", 5),
            ("year", 3),
            ("engine_volume", 7),
            ("brand", 10),
            ("price", 1),
            ("year", 30),
            ("engine_volume", 25),
        ],
        ids=[
            "sort_price_limit5",
            "sort_year_limit3",
            "sort_engine_volume_limit7",
            "sort_brand_limit10",
            "sort_price_limit1",
            "sort_year_limit30_overflow",
            "sort_engine_volume_limit25_all",
        ],
    )
    def test_search_cars(self, authed_session: requests.Session, sort_by, limit):
        params = {"sort_by": sort_by, "limit": limit}

        LOGGER.info("GET %s params=%s", CARS_ENDPOINT, params)
        resp = authed_session.get(CARS_ENDPOINT, params=params, timeout=10)

        LOGGER.debug("Status=%s Body=%s", resp.status_code, resp.text)
        assert resp.status_code == 200, f"Search failed: {resp.status_code}, body={resp.text}"

        cars = resp.json()
        assert isinstance(cars, list), f"Expected list, got: {type(cars)}"

        expected_len = min(limit, TOTAL_CARS_IN_DB)
        assert len(cars) == expected_len, f"Expected {expected_len} cars, got {len(cars)}"

        for car in cars:
            assert sort_by in car, f"Missing '{sort_by}' in car item: {car}"

        assert_sorted(cars, sort_by)

    def test_get_cars_sorted_by_price_limit_10(self, authed_session: requests.Session):
        LOGGER.info("GET /cars?sort_by=price&limit=10")

        resp = authed_session.get(
            CARS_ENDPOINT,
            params={"sort_by": "price", "limit": 10},
            timeout=10
        )

        LOGGER.info("Response status: %s", resp.status_code)
        assert resp.status_code == 200

        cars = resp.json()
        assert isinstance(cars, list)
        assert len(cars) == 10

        prices = [car["price"] for car in cars]
        assert prices == sorted(prices)
