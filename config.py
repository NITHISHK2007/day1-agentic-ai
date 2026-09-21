import os
from dotenv import load_dotenv

load_dotenv()

PROVIDER = os.getenv("PROVIDER")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL")
COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}