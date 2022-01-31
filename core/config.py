from starlette.config import Config


config = Config(".env")

DATABASE_URL = config("MR_DATABASE_URL", cast=str, default="")
