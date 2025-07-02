# EduChain MCP Server

Hello, My name is Meet Patel.
This project demonstrates my ability to build a **Model Context Protocol (MCP)** server using the **EduChain** library and integrate it with external tools for educational content generation.

---

## 🚀 Objective

Build an **MCP-compliant server** using the [EduChain](https://github.com/satvik314/educhain) library that:
- Generates educational content (MCQs, lesson plans)
- Exposes them via HTTP endpoints
- Can integrate with tools like Claude Desktop (via MCP spec)

---

## 📁 Repository Structure

```
ai_intern_assignment/
├── test_educhain.py          # Test EduChain integration
├── mcp_server.py             # Main MCP server using Flask
├── test_api.py               # Manual API testing script
├── Sample_Responses.txt      # Example inputs & outputs
└── README.md                 # This file
```

---

> ⚠️ IMPORTANT: For security reasons, my API key is not included.
> Please replace the placeholder in `mcp_server.py` and `test_educhain.py` with your own Gemini API key from https://aistudio.google.com/app/apikey

---

## ✅ Task Breakdown

### 🧩 Task 1: Set Up the EduChain Environment

- ✅ Installed EduChain and dependencies
- ✅ Integrated EduChain using Gemini API (Google)
- ✅ Tested generation of:
  - Multiple-choice questions (MCQs)
  - Lesson plans
- ✅ Sample topic used: `"Python Programming Basics"`

> 📎 **Citation**: EduChain documentation from [satvik314/educhain](https://github.com/satvik314/educhain)

### ⚙️ Task 2: Build the MCP Server with EduChain

- ✅ Built Flask server in Python
- ✅ Created two HTTP tools:
  - `/generate_mcq`: Generates MCQs based on topic + count
  - `/lesson_plan`: Returns a structured lesson plan for a subject
- ✅ Responses are returned in clean JSON format
- ✅ Tools follow MCP-compatible input schema

> 📎 **Citation**: Claude MCP server logic adapted to HTTP-compatible endpoints (in absence of official Claude SDK)

### 🧪 Task 3: Test the MCP Server

- ✅ Used Python's `requests` library to test endpoints manually
- ✅ Verified server response matches expected EduChain outputs
- ❌ Claude Desktop was not tested due to system compatibility issues (not mandatory)

---

## 🧾 Sample Commands & Responses

Refer to the [Sample_Responses.txt](./Sample_Responses.txt) file for:

- Input JSON requests for each tool
- JSON output from the server

---

## 🎁 Bonus (Optional Points)

- [x] MCP Server includes **2 tools** (MCQ + Lesson Plan)
- [x] Uses **Gemini API (free)** for educational content generation
- [ ] Video Walkthrough (Optional – Not created due to time constraints)

---

## 🧪 Requirements Met

| Requirement                   | Status  |
|-------------------------------|---------|
| Code Documentation            | ✅ Done |
| Proper Citation               | ✅ Done |
| JSON-formatted Outputs        | ✅ Done |
| GitHub Repo with All Files    | ✅ Done |
| Sample Commands and Outputs   | ✅ Done |
| Claude Integration Attempted  | ❌ Skipped |

---

## 🧠 Tools Used

- [EduChain](https://github.com/satvik314/educhain)
- [Flask](https://flask.palletsprojects.com/)
- [Google Gemini API](https://aistudio.google.com/app/apikey)
- ChatGpt
- Python 3.11
- Visual Studio Code

---

## 📜 License

This project uses public open-source tools and APIs. EduChain is credited and linked. No proprietary code has been used.
