import os
from dotenv import load_dotenv

load_dotenv()


def is_enabled(value, default):
    if isinstance(value, str):
        if value.lower() in ["true", "yes", "1", "enable", "y"]:
            return True
        elif value.lower() in ["false", "no", "0", "disable", "n"]:
            return False
    return default


# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", 26975590))  # Default to 0 if not set
API_HASH = os.environ.get("API_HASH", "9fa30733d7a99b212485393e6b5c5ceb")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7065180942:AAEqo9Tn0PMpdLjBfk-wYO2DNZ80gygsXMA")  # Bot token from @BotFather
ADMINS = (
    [int(i.strip()) for i in os.environ.get("ADMINS", "5827289728").split(",")]
    if os.environ.get("ADMINS")
    else []
)

DATABASE_NAME = os.environ.get("DATABASE_NAME", "Shortnerbot")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://shortnerbot:GkeGvUjcRGOunkoi@shortnerbot.cfwbjti.mongodb.net/?retryWrites=true&w=majority&appName=Shortnerbot")  # MongoDB URI
OWNER_ID = int(os.environ.get("OWNER_ID", 7272399911))  # Default to 0 if not set
if OWNER_ID and OWNER_ID not in ADMINS:
    ADMINS.append(OWNER_ID)

# Optional variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002434243644"))  # Default to 0
UPDATE_CHANNEL = int(os.environ.get("UPDATE_CHANNEL", "-1002434243644"))  # Default to 0
BROADCAST_AS_COPY = is_enabled(os.environ.get("BROADCAST_AS_COPY", "False"), False)
IS_PRIVATE = is_enabled(os.environ.get("IS_PRIVATE", "False"), False)
SOURCE_CODE = os.environ.get("SOURCE_CODE", "https://t.me/Soutick_09")
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", "")
LINK_BYPASS = is_enabled(os.environ.get("LINK_BYPASS", "False"), False)
BASE_SITE = os.environ.get("BASE_SITE", "rglinks.com")

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

FORWARD_MESSAGE = is_enabled(os.environ.get("FORWARD_MESSAGE", "True"), True)

# Web server settings
WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "True"), True)
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "240"))
PORT = int(os.environ.get("PORT", "8000"))

# Validate mandatory variables
if not API_ID or not API_HASH or not BOT_TOKEN:
    raise ValueError("Missing mandatory environment variables: API_ID, API_HASH, BOT_TOKEN.")
