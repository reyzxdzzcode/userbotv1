import os

DEVS = [
    6995861464,
]

API_ID = int(os.getenv("API_ID", "23347872"))

API_HASH = os.getenv("API_HASH", "f8310b4684c1d34d69f0d9b546de9a11")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6352133040:AAGnIcyKKJ_FgkoHjLeIJqiiEZ_IuN8Hnug")

OWNER_ID = int(os.getenv("OWNER_ID", "6995861464"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002319319648"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002436221538").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "550"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "sk-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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://dantesbot:wildan18@cluster0.fol5tml.mongodb.net/?retryWrites=true&w=majority",
)


