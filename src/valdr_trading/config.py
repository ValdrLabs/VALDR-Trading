import os

from dotenv import load_dotenv


load_dotenv()


class Settings:

    DATA_PROVIDER = os.getenv("DATA_PROVIDER", "massive")
    MASSIVE_API_KEY = os.getenv("MASSIVE_API_KEY")