from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
import requests
import string
import aiohttp
import asyncio
from devgagan import app
from devgagan.core.func import *
from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB, WEBSITE_URL, AD_API, LOG_GROUP, UPDATES, OWNER
from shortzy import Shortzy
 
 
tclient = AsyncIOMotorClient(MONGO_DB)
tdb = tclient["telegram_bot"]
token = tdb["tokens"]
 
 
async def create_ttl_index():
    await token.create_index("expires_at", expireAfterSeconds=0)
 
 
 
Param = {}
 
 
async def generate_random_param(length=8):
    """Generate a random parameter."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
 
 
async def get_shortened_url(deep_link):
    shortzy = Shortzy(api_key=AD_API, base_site=WEBSITE_URL)
    shortened_url = await shortzy.convert(deep_link)
    return shortened_url    
 
async def is_user_verified(user_id):
    """Check if a user has an active session."""
    session = await token.find_one({"user_id": user_id})
    return session is not None
 
 
@app.on_message(filters.command("start"))
async def token_handler(client, message):
    """Handle the /token command."""
    join = await subscribe(client, message)
    if join == 1:
        return

    # Define your inline keyboard buttons
    join_button = InlineKeyboardButton("Join Channel", url=f"https://t.me/{UPDATES}")
    premium_button = InlineKeyboardButton("Get Premium", url=f"https://t.me/{OWNER}")
    keyboard = InlineKeyboardMarkup([
        [join_button],
        [premium_button]
    ])

    # Your message text
    text = (
        "𝑯𝒆𝒚!...... \n\n"
        "📌 𝑾𝒂𝒏𝒏𝒂 𝒌𝒏𝒐𝒘 𝒂𝒃𝒐𝒖𝒕 𝒎𝒆? 𝑰𝒎 𝒂𝒏 𝒂𝒅𝒗𝒂𝒏𝒄𝒆 𝒓𝒆𝒔𝒕𝒓𝒊𝒄𝒕𝒆𝒅 𝑪𝒐𝒏𝒕𝒆𝒏𝒕 𝑺𝒂𝒗𝒆𝒓 𝒃𝒐𝒕 𝒘𝒊𝒕𝒉 𝒂 𝒇𝒂𝒔𝒕 𝒔𝒑𝒆𝒆𝒅!\n"
        "📌 𝑾𝒂𝒏𝒏𝒂 𝒌𝒏𝒐𝒘 𝒂𝒃𝒐𝒖𝒕 𝒎𝒚 𝒄𝒐𝒎𝒎𝒂𝒏𝒅𝒔? 𝑼𝒔𝒆 /help 𝒕𝒐 𝒇𝒊𝒏𝒅 𝒕𝒉𝒆𝒎 𝒐𝒖𝒕!"
    )

    # Send just the text with the keyboard
    await message.reply(
        text,
        reply_markup=keyboard
    )
    return
    
    param = message.command[1] if len(message.command) > 1 else None
    freecheck = await chk_user(message, user_id)
    if freecheck != 1:
        await message.reply("You are a premium user no need of token 😉")
        return
 
     
    if param:
        if user_id in Param and Param[user_id] == param:
             
            await token.insert_one({
                "user_id": user_id,
                "param": param,
                "created_at": datetime.utcnow(),
                "expires_at": datetime.utcnow() + timedelta(hours=3),
            })
            del Param[user_id]   
            await message.reply("✅ You have been verified successfully! Enjoy your session for next 3 hours.")
            return
        else:
            await message.reply("❌ Invalid or expired verification link. Please generate a new token.")
            return
 
@app.on_message(filters.command("token"))
async def smart_handler(client, message):
    user_id = message.chat.id
     
    freecheck = await chk_user(message, user_id)
    if freecheck != 1:
        await message.reply("You are a premium user no need of token 😉")
        return
    if await is_user_verified(user_id):
        await message.reply("✅ Your free session is already active enjoy!")
    else:
         
        param = await generate_random_param()
        Param[user_id] = param   
 
         
        deep_link = f"https://t.me/{client.me.username}?start={param}"
 
         
        shortened_url = await get_shortened_url(deep_link)
        if not shortened_url:
            await message.reply("❌ Failed to generate the token link. Please try again.")
            return
 
         
        button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Verify", url=shortened_url)]]
        )
        await message.reply("Click the button below to verify your free access token: \n\n> What will you get ? \n1. No time bound upto 3 hours \n2. Batch command limit will be FreeLimit + 20 \n3. All functions unlocked", reply_markup=button)
 
