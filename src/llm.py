from groq import Groq
from src.config import GROQ_API_KEY


llm_client = Groq(
    api_key = GROQ_API_KEY
)