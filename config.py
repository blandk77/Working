from os import getenv 

# Compulsary!!
API_ID = int(getenv("API_ID", "27394279"))
API_HASH = getenv("API_HASH", "90a9aa4c31afa3750da5fd686c410851")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))

#Mongodb 
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://telegramguy21:tnkIwvbNkJ5U3fZ7@botsuse.bpgag.mongodb.net/?retryWrites=true&w=majority&appName=Botsuse")
DATABASE_NAME = getenv("DATABASE_NAME", "Demo") 

#Logs channel and fsub
LOG_GROUP = getenv("LOG_GROUP", "-1002288135729")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))

# Optional...

#Session string 
STRING = getenv("STRING", None)
# Limits 
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "100"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))

# Shortener
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")

#Nothing to fill here
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""
