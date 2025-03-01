import _setup_tests


def test_invalid_tokens(utilities_function, tokens, error_msg, **kwargs):
    function_name = utilities_function.__name__
    try:
        utilities_function(tokens, **kwargs)
        print(f"Verified that {function_name}() does not crash when {error_msg}\n")
    except:
        print(f"Failed test case: {function_name}() crashes when {error_msg}\n")


def test_utilities(client):
    utilities = client.utilities

    search_response = utilities.web_search(["AI", "Library"])  # Perform a web search
    print(f"utilities.web_search() response:\n{search_response}\n\n\n\n")

    parser_response = utilities.web_parser(["https://www.ailibrary.ai"])  # Parse web pages
    print(f"utilities.web_parser() response \n{parser_response}\n\n\n\n")

    news_search_response = utilities.news_search(["artificial intelligence", "nba"])
    print(f"utilities.news_search() response \n{news_search_response}\n\n\n\n")

    url = "https://assets.ctfassets.net/416ywc1laqmd/2funRKZhiiWEzKLRCkJsBx/"+ \
        "edb10d102665a99a0a3824d0806c02ca/Sched_TOC.pdf"
    doc_parser_response = utilities.document_parser([url])
    print(f"utilities.document_parser() response \n{doc_parser_response}\n\n\n\n")

    doc_thumbnail_response = utilities.document_thumbnail([url])
    print(f"utilities.document_thumbnail() response \n{doc_thumbnail_response}\n\n\n\n")

    instruction = "Please generate a form with the following fields: \n name (string), email(string), phone(number), experience in years (number), ai experience in years (number), highest educational qualification (phd, bachelor's degree, high school, not mentioned)"
    schema_gen_response = utilities.json_schema_generator(instruction)
    print(f"utilities.json_schema_generator() response \n{schema_gen_response}\n\n")

    validator_response = utilities.json_schema_validator(schema_gen_response)
    print(f"utilities.json_schema_validator() response \n{validator_response}\n\n")

    for url_function in [utilities.web_parser, utilities.document_parser, utilities.document_thumbnail]:
        test_invalid_tokens(url_function, ["doesnotexist.com"], "a given url does not exist")
        test_invalid_tokens(url_function, ["not_even_a_url .com"], "a given url is an invalid link")

    test_invalid_tokens(utilities.web_search, ["https://ailibrary.ai", "https://doesnotexist.com"], 
                        "given search terms are actually urls")

    test_invalid_tokens(utilities.news_search, ["https://ailibrary.ai", "https://doesnotexist.com"], 
                        "given search terms are actually urls")


if __name__ == "__main__":
    client = _setup_tests.__setup()
    print("Running test_utilities:\n")
    test_utilities(client)
    print("Finished running test_utilities\n")
