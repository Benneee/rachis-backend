import os

environment = os.getenv("ENV", "development")

if environment == "development":
    from settings.development import *

    