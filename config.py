from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","23053980"))
API_HASH = getenv("API_HASH", "9f7cb9215fa0007089951c86d31d0128")

BOT_TOKEN = getenv("BOT_TOKEN", "7084577439:AAE9EekElY9fCcuVd-JaxLJ44Iaw2ePbGLw")
OWNER_ID = int(getenv("OWNER_ID", "5685358346"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://vedant12ok:vedant@cluster0.hknrwrr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN", None)
