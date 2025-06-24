import os 
from dotenv import load_dotenv

# Load environment variables from .env file
class Settings:
    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
settings = Settings()