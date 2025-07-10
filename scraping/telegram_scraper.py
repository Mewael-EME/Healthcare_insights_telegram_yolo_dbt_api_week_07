import os
import json
import asyncio
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto
from telethon.errors import FloodWaitError
from dotenv import load_dotenv
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load API credentials from .env file
load_dotenv()

api_id_raw = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone = os.getenv("PHONE_NUMBER")

print("Loaded API_ID:", api_id_raw)  # Debug

if not api_id_raw or not api_hash:
    raise EnvironmentError("Missing API_ID or API_HASH in .env file")

API_ID = int(api_id_raw)
API_HASH = api_hash
PHONE_NUMBER = phone

# ✅ FIX: Add the channel list here
CHANNELS = [
    "https://t.me/lobelia4cosmetics",
    "https://t.me/tikvahpharma",
    "https://t.me/Chemed"
]

async def scrape_all_channels(client):
    date_str = datetime.utcnow().strftime("%Y-%m-%d")
    for channel_url in CHANNELS:
        folder_path = os.path.join("data", "raw", "telegram_messages", date_str)
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, f"{channel_url.split('/')[-1]}.json")
        messages_data = []

        try:
            entity = await client.get_entity(channel_url)
            async for message in client.iter_messages(entity, limit=200):
                if message:
                    data = {
                        "id": message.id,
                        "date": str(message.date),
                        "text": message.message,
                        "has_image": isinstance(message.media, MessageMediaPhoto),
                        "media_path": None
                    }

                    if data["has_image"]:
                        media_dir = os.path.join(folder_path, "media")
                        os.makedirs(media_dir, exist_ok=True)
                        img_path = os.path.join(media_dir, f"{message.id}.jpg")
                        await client.download_media(message.media, file=img_path)
                        data["media_path"] = img_path

                    messages_data.append(data)

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(messages_data, f, ensure_ascii=False, indent=2)

            logging.info(f"Scraped {len(messages_data)} messages from {channel_url}")
        except Exception as e:
            logging.error(f"Error scraping {channel_url}: {e}")

async def main():
    async with TelegramClient("session_kaim", API_ID, API_HASH) as client:
        await scrape_all_channels(client)

def run():
    asyncio.run(main())

if __name__ == "__main__":
    run()
