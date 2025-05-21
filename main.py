import config
import time
import logging
import asyncio
import threading
from pyrogram import Client, idle
from pyromod import listen
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from fastapi import FastAPI
import uvicorn

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

StartTime = time.time()
app = Client(
    "Anonymous",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="StringGenBot"),
)

api = FastAPI()

@api.get("/")
@api.get("/health")
async def health_check():
    return {"status": "ok", "bot": app.me.username if app.me else "offline"}

def start_fastapi():
    uvicorn.run(api, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    print("Starting the String Generator Bot...")
    try:
        app.start()
        app.me = app.get_me()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    
    print(f"@{app.me.username} started successfully!")

    # Start FastAPI server in a separate thread
    threading.Thread(target=start_fastapi).start()

    idle()
    app.stop()
    print("Bot stopped. Bye!")
