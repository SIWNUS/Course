from dotenv import load_dotenv
import os

load_dotenv("../.env")

phone = os.getenv("PHONE_NUMBER")
print(type(phone))
