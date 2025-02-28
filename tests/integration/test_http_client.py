import pytest

@pytest.mark.order(0)  # This ensures it runs first
class TestHTTPClientInit:
    # general case
    # empty api key
    # empty base url
    # empty version
    # base url with and without slash
    # version with and without slash
    def test_general(self):
        pass


@pytest.mark.order(1)  # This ensures it runs second
class TestHTTPClientRequest:
    # general case per method
    # invalid method
    # invalid url
    # invalid params
    # invalid data
    # invalid json
    # invalid files


    def test_general(self):
        pass

