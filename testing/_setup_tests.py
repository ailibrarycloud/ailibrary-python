import ailibrary as ai
from dotenv import load_dotenv
import os

def __setup():
    """ Setup function for tests """
    load_dotenv()
    api_key = os.environ["DEV_KEY"]
    domain = "https://5b18-2600-1700-5430-cd70-fd23-dbc3-3caa-fa33.ngrok-free.app"
    client = ai.AILibrary(api_key, domain)
    return client


if __name__ == "__main__":
    client = __setup()
    print(client)