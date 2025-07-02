import requests

# Testing /generate_mcq
response = requests.post("http://127.0.0.1:5000/generate_mcq", json={
    "topic": "Python Loops",
    "num": 5
})
print("MCQ Response:")
print(response.json())

# Testing /lesson_plan
response = requests.post("http://127.0.0.1:5000/lesson_plan", json={
    "topic": "Algebra"
})
print("\nLesson Plan Response:")
print(response.json())
