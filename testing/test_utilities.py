import _setup_tests


def test_utilities(client):
    utilities = client.utilities

    search_response = utilities.web_search(["AI", "Library"])  # Perform a web search
    print(f"utilities.web_search() response: {search_response}")

    parser_response = utilities.web_parser(["https://example.com"])  # Parse web pages
    print(f"utilities.web_parser() response: {parser_response}")


if __name__ == "__main__":
    client = _setup_tests.__setup()
    print("Running test_utilities:")
    test_utilities(client)
    print("Finished running test_utilities")
