from educhain import Educhain, LLMConfig
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# 🔐 NOTE: Replace this with your own Gemini API key
os.environ["GOOGLE_API_KEY"] = "my_api_is_hidden_please_use_your_own" 
# using gemini api as its free

# Gemini model
gemini = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

# Creating EduChain client with Gemini
config = LLMConfig(custom_model=gemini)
client = Educhain(config)

# Generating questions
questions = client.qna_engine.generate_questions(
    topic="Python Programming Basics",
    num=5
)

print(questions.model_dump_json())
