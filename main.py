from generator import generate_questions

with open("sample.txt", "r") as f:
    text = f.read()

qs = generate_questions(text)

print("\nGenerated Questions:\n")
for i, q in enumerate(qs, 1):
    print(f"{i}. {q}")
