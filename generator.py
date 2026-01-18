import random

def generate_questions(text):
    lines = text.split(".")
    questions = []

    for line in lines:
        line = line.strip()
        if len(line.split()) > 6:
            questions.append(f"What is meant by: {line[:40]}...?")

    return random.sample(questions, min(5, len(questions)))
