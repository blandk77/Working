from pyrogram import filters
from devgagan import app
from config import OWNER_ID, OWNER, PLAN_USD, PLAN_INR
from devgagan.core.func import subscribe
import asyncio
from devgagan.core.func import *
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.raw.functions.bots import SetBotInfo
from pyrogram.raw.types import InputUserSelf

from pyrogram.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
 
@app.on_message(filters.command("set"))
async def set(_, message):
    if message.from_user.id not in OWNER_ID:
        await message.reply("You are not authorized to use this command.")
        return
     
    await app.set_bot_commands([
        BotCommand("start", "Check if Im alive or not ⚡"),
        BotCommand("settings", "Personalize User settings (Thumbnail, replace words, caption, etc)"),
        BotCommand("token", "Get 3 hours free access 😉 (use without time intervals)"),
        BotCommand("help", " Learn how to use me!"),
        BotCommand("cancel", "🚫 Cancel batch or any ongoing process"),
        BotCommand("batch", "Download videos in bulk"),
        BotCommand("login", "Connect your TG account with bot 🌅"),
        BotCommand("logout", "Delete your account access in the bot 🌄"),
        BotCommand("plan", "Check our premium plans 🤑"),
        BotCommand("terms", "Terms and conditions 📜"),
        BotCommand("transfer", "💘 Gift premium to others (Only if you have bot premium)"),
        BotCommand("myplan", "⌛ Get your plan details"),
        BotCommand("session", "🧵 Generate Pyrogramv2 session"),
        BotCommand("add", "➕ Add user to premium [OWNER]"),
        BotCommand("rem", "➖ Remove from premium [OWNER]"),
        BotCommand("freez", "Remove all expired user 💔 [OWNER]"),
        BotCommand("stats", "📊 Get stats of the bot (OWNER)"),
        BotCommand("speedtest", "🚅 Speed of server (OWNER)"),
        BotCommand("lock", "🔒 Protect channel from extraction (OWNER("),
        BotCommand("gcast", "⚡ Broadcast message to bot users (OWNER)")
    ])
 
    await message.reply("✅ Commands configured successfully!")
 
 
 
 
help_pages = [
    (
        "Usᴇʀ ᴄᴏᴍᴍᴀɴᴅs:\n\n__/login__\n**» Log into the bot for private channel access 🌄**\n\n__/batch__\n**» Bulk extraction for posts (after login) ⚡**\n\n__/logout__\n**» Logout from the bot 🌅**\n\n__/plan__\n**» Check available premium plans 💰😁**\n\n__/terms__\n**» View terms 📜 and conditions ©️**\n\n__/cancel__\n**» Cancel ongoing batch process 🔚**\n\n__/myplan__\n**» Get details about your plan expiry date 🌹**\n\n__/transfer userID__\n**» Transfer premium to another user 🔄 (Premium Users Only)**\n\n__/session__\n**» Generate Pyrogram V2 session 🧵**\n\n__/settings__\n» **Advanced customization ⚙️ (See usage below 👇)**\n\n__**Settings usage:**__\n📌 `SETCHATID` : __Direct uploads to channel/group/user with -100[chatID]__\n📌 `SETRENAME` : __Add custom rename tag or channel username__\n📌 `CAPTION` : __Add a custom caption to uploads__\n📌 `REPLACEWORDS` : __Replace specific words in your content__\n**Etc....**"

    ),
    (
        "𝑂𝑤𝑛𝑒𝑟 𝐶𝑜𝑚𝑚𝑎𝑛𝑑𝑠:\n\n__/add userID__\n**» Add a user to premium (__Owner only__)**\n\n__/rem userID__\n\n**» Remove a user from premium (__Owner only__)**\n\n__/get__\n**» Get all user IDs (__Owner only__)**\n\n__/lock Channel_id__\n**» Lock a channel from extraction (__Owner only__)**\n\n__/stats__\n**» Get bot statistics (__Owner only__)**\n\n__/speedtest__\n**» Test the server speed (__Owner only__)**"
    )
]
 
 
async def send_or_edit_help_page(_, message, page_number):
    if page_number < 0 or page_number >= len(help_pages):
        return
 
     
    prev_button = InlineKeyboardButton("Usᴇʀ ᴄᴏᴍᴍᴀɴᴅs", callback_data=f"help_prev_{page_number}")
    next_button = InlineKeyboardButton("𝑂𝑤𝑛𝑒𝑟 𝐶𝑜𝑚𝑚𝑎𝑛𝑑𝑠", callback_data=f"help_next_{page_number}")
 
     
    buttons = []
    if page_number > 0:
        buttons.append(prev_button)
    if page_number < len(help_pages) - 1:
        buttons.append(next_button)
 
     
    keyboard = InlineKeyboardMarkup([buttons])
 
     
    await message.delete()
 
     
    await message.reply(
        help_pages[page_number],
        reply_markup=keyboard
    )
 
 
@app.on_message(filters.command("help"))
async def help(client, message):
    join = await subscribe(client, message)
    if join == 1:
        return
 
     
    await send_or_edit_help_page(client, message, 0)
 
 
@app.on_callback_query(filters.regex(r"help_(prev|next)_(\d+)"))
async def on_help_navigation(client, callback_query):
    action, page_number = callback_query.data.split("_")[1], int(callback_query.data.split("_")[2])
 
    if action == "prev":
        page_number -= 1
    elif action == "next":
        page_number += 1
 
     
    await send_or_edit_help_page(client, callback_query.message, page_number)
 
     
    await callback_query.answer()
 
 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 
@app.on_message(filters.command("terms") & filters.private)
async def terms(client, message):
    terms_text = (
        "> 📜 **Terms and Conditions** 📜\n\n"
        "✨ We are not responsible for user deeds, and we do not promote copyrighted content. If any user engages in such activities, it is solely their responsibility.\n"
        "✨ Upon purchase, we do not guarantee the uptime, downtime, or the validity of the plan. __Authorization and banning of users are at our discretion; we reserve the right to ban or authorize users at any time.__\n"
        "✨ Payment to us **__does not guarantee__** authorization for the /batch command. All decisions regarding authorization are made at our discretion\n"
    )
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📋 See Plans", callback_data="see_plan")],
            [InlineKeyboardButton("💬 Contact Now", url=f"https://t.me/{OWNER}")],
        ]
    )
    await message.reply_text(terms_text, reply_markup=buttons)
 
 
@app.on_message(filters.command("plan") & filters.private)
async def plan(client, message):
    plan_text = (
        f"> 💰 **Premium Price**:\n\n Starting from ${PLAN_USD} or  {PLAN_INR}INR accepted via **__Crypto And UPI__** (terms and conditions apply).\n"
        "📥 **Download Limit**: Users can download up to 100,000 files in a single batch command.\n"
        "🛑 **Batch**: You will get two modes /bulk and /batch.\n"
        "   - Users are advised to wait for the process to automatically cancel before proceeding with any downloads or uploads.\n\n"
        "📜 **Terms and Conditions**: For further details and complete terms and conditions, please send /terms.\n"
    )
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📜 See Terms", callback_data="see_terms")],
            [InlineKeyboardButton("💬 Contact Now", url=f"https://t.me/{OWNER}")],
        ]
    )
    await message.reply_text(plan_text, reply_markup=buttons)
 
 
@app.on_callback_query(filters.regex("see_plan"))
async def see_plan(client, callback_query):
    plan_text = (
        f"> 💰**Premium Price**\n\n Starting from ${PLAN_USD} or {PLAN_INR} INR accepted via **__Crypto and UPI__** (terms and conditions apply).\n"
        "📥 **Download Limit**: Users can download up to 100,000 files in a single batch command.\n"
        "🛑 **Batch**: You will get two modes /bulk and /batch.\n"
        "   - Users are advised to wait for the process to automatically cancel before proceeding with any downloads or uploads.\n\n"
        "📜 **Terms and Conditions**: For further details and complete terms and conditions, please send /terms or click See Terms👇\n"
    )
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📜 See Terms", callback_data="see_terms")],
            [InlineKeyboardButton("💬 Contact Now", url=f"https://t.me/{OWNER}")],
        ]
    )
    await callback_query.message.edit_text(plan_text, reply_markup=buttons)
 
 
@app.on_callback_query(filters.regex("see_terms"))
async def see_terms(client, callback_query):
    terms_text = (
        "> 📜 **Terms and Conditions** 📜\n\n"
        "✨ We are not responsible for user deeds, and we do not promote copyrighted content. If any user engages in such activities, it is solely their responsibility.\n"
        "✨ Upon purchase, we do not guarantee the uptime, downtime, or the validity of the plan. __Authorization and banning of users are at our discretion; we reserve the right to ban or authorize users at any time.__\n"
        "✨ Payment to us **__does not guarantee__** authorization for the /batch command. All decisions regarding authorization are made at our discretion and mood.\n"
    )
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📋 See Plans", callback_data="see_plan")],
            [InlineKeyboardButton("💬 Contact Now", url=f"https://t.me/{OWNER}")],
        ]
    )
    await callback_query.message.edit_text(terms_text, reply_markup=buttons)
 
 
