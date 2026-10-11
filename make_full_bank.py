import json

# Load base 75 questions from generate_bank.py
import generate_bank
questions = generate_bank.questions

print(f"Starting with {len(questions)} base questions.")

# Function to add questions
def add(module, q_text, options, correct_idx, explanation, difficulty="Medium"):
    questions.append({
        "id": len(questions) + 1,
        "module": module,
        "question": q_text,
        "options": options,
        "correct": correct_idx,
        "explanation": explanation,
        "difficulty": difficulty
    })

# Add comprehensive questions for all modules
# Let's add questions in batches for each module

