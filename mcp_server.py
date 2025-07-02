from flask import Flask, request, jsonify
from educhain import Educhain, LLMConfig
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Initializing Flask app
app = Flask(__name__)
  
# 🔐 NOTE: Replace this with your own Gemini API key
os.environ["GOOGLE_API_KEY"] = "my_api_is_hidden_please_use_your_own"
# using gemini api as its free

# Gemini model
gemini = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

gemini.__class__.model_rebuild()

# EduChain Setup with Gemini
config = LLMConfig(custom_model=gemini)
client = Educhain(config)

# Route 1: Generating MCQs
@app.route('/generate_mcq', methods=['POST'])
def generate_mcq():
    data = request.json
    topic = data.get("topic", "Python Basics")
    num = data.get("num", 5)

    try:
        questions = client.qna_engine.generate_questions(topic=topic, num=num)
        return jsonify(questions.model_dump())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route 2: Generating Lesson Plan
@app.route('/lesson_plan', methods=['POST'])
def lesson_plan():
    data = request.json
    topic = data.get("topic", "Algebra")

    try:
        plan = client.content_engine.generate_lesson_plan(topic=topic)
        return jsonify(plan.model_dump())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ping endpoint
@app.route("/", methods=["GET"])
def index():
    return "✅ MCP Server Running with EduChain + Gemini"

# Starting the server
if __name__ == '__main__':
    app.run(port=5000, debug=True)
