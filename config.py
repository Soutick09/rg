import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv("soutick.env")


# Debug: Print environment variables to verify they are loaded
print("API_ID:", os.getenv("API_ID"))
print("API_HASH:", os.getenv("API_HASH"))
print("BOT_TOKEN:", os.getenv("BOT_TOKEN"))

def is_enabled(value, default):
    if isinstance(value, str):
        if value.lower() in ["true", "yes", "1", "enable", "y"]:
            return True
        elif value.lower() in ["false", "no", "0", "disable", "n"]:
            return False
    return default


# Mandatory variables for the bot to start
# API ID from https://my.telegram.org/auth
API_ID = int(os.environ.get("API_ID", 0))  # Default to 0 if not set
API_HASH = os.environ.get("API_HASH", "")  # Empty string as default
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")  # Empty string as default

ADMINS = (
    [int(i.strip()) for i in os.environ.get("ADMINS", "").split(",")]
    if os.environ.get("ADMINS")
    else []
)

DATABASE_NAME = os.environ.get("DATABASE_NAME", "Shortnerbot")
DATABASE_URL = os.environ.get("DATABASE_URL", "")  # Default to empty if not set
OWNER_ID = int(os.environ.get("OWNER_ID", 0))  # Default to 0 if not set
if OWNER_ID and OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)

# Optional variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))  # Default to 0
UPDATE_CHANNEL = int(os.environ.get("UPDATE_CHANNEL", "0"))  # Default to 0
BROADCAST_AS_COPY = is_enabled(os.environ.get("BROADCAST_AS_COPY", "False"), False)
IS_PRIVATE = is_enabled(os.environ.get("IS_PRIVATE", "False"), False)
SOURCE_CODE = os.environ.get("SOURCE_CODE", "https://github.com/kevinnadar22/URL-Shortener-V2")
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", "")
LINK_BYPASS = is_enabled(os.environ.get("LINK_BYPASS", "False"), False)
BASE_SITE = os.environ.get("BASE_SITE", "droplink.co")

# For Admin use
CHANNELS = is_enabled(os.environ.get("CHANNELS", "True"), True)
CHANNEL_ID = (
    [int(i.strip()) for i in os.environ.get("CHANNEL_ID", "").split(",")]
    if os.environ.get("CHANNEL_ID")
    else []
)

DE_BYPASS = (
    [i.strip() for i in os.environ.get("DE_BYPASS", "").split(",")]
    if os.environ.get("DE_BYPASS")
    else []
)
DE_BYPASS.append("mdisk.me")

FORWARD_MESSAGE = is_enabled(os.environ.get("FORWARD_MESSAGE", "False"), False)

# Web server settings
WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "True"), True)
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "240"))  # Default to 240 seconds
PORT = int(os.environ.get("PORT", "8000"))  # Default to port 8000

# Validate mandatory variables
if not API_ID or not API_HASH or not BOT_TOKEN:
    raise ValueError("Missing mandatory environment variables: API_ID, API_HASH, BOT_TOKEN.")
