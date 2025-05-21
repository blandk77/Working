from os import getenv 

# Compulsary!!
API_ID = int(getenv("API_ID", "27394279"))
API_HASH = getenv("API_HASH", "90a9aa4c31afa3750da5fd686c410851")
BOT_TOKEN = getenv("BOT_TOKEN", "7721902522:AAHamnJnM9f1AjWPvhl4NpzLeoM_d5TW6Dw")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1705634892").split()))

#Mongodb 
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://telegramguy21:tnkIwvbNkJ5U3fZ7@botsuse.bpgag.mongodb.net/?retryWrites=true&w=majority&appName=Botsuse")
DATABASE_NAME = getenv("DATABASE_NAME", "Demo") 

#Logs channel and fsub
LOG_GROUP = getenv("LOG_GROUP", "-1002288135729")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002226481922"))

#Usernames
OWNER = getenv("OWNER", "Itsme123i")
UPDATES = getenv("UPDATES", "the_tgguy")

#PLAN PRICES 
PLAN_USD = int(getenv("PLAN_USD", "3"))
PLAN_INR = int(getenv("PLAN_INR", "200"))
REMOVE_THUMB = False
# Optional...

#Session string 
STRING = getenv("STRING", None)
# Limits 
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "100"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))

# Shortener
WEBSITE_URL = getenv("WEBSITE_URL", "linkmonetizer.in")
AD_API = getenv("AD_API", "bf35b33b841943cdce510413393f35a9ff0bb558")

#Pic for settings 
SET_PIC = getenv("SET_PIC", "https://files.catbox.moe/8ol7bs.jpg")

#Nothing to fill here
INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)

