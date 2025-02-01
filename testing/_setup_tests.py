import ailibrary as ai
from dotenv import load_dotenv
import os

def __setup():
    """ Setup function for tests """
    load_dotenv()
    api_key = os.environ["DEV_KEY"]
    client = ai.AILibrary(api_key)
    
    return client

