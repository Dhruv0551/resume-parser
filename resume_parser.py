from dotenv import load_dotenv
import os
from pypdf import PdfReader
from groq import Groq
import json

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
