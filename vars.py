

from os import environ

API_ID = int(environ.get("API_ID", "29978901"))
API_HASH = environ.get("API_HASH", "500fc876c5356cf04ed3698912dc2edf")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "bot_subscription")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/bot_subscription")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "5776977809").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "5776977809"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://rupakaryanaryan:rupakaryanaryan@cluster0.05xkjx2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")






