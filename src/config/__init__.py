import os

from dotenv import load_dotenv

from .schemas import DBSettings, BotSettings


load_dotenv()

db_settings = DBSettings(
    db_connection_string=os.getenv("MONGODB_CONNECTION_STRING"),
    db_name=os.getenv("DATABASE_NAME")
)

bot_settings = BotSettings(
    token=os.getenv("BOT_TOKEN")
)
