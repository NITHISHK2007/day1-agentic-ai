from agent import agent
questions = [
    "What is the fee for AI202?",
    "What is the fee for DS303?",
    "What is the total fee for CS101 and AI202 after a 10% scholarship?",
    "Give me a 2-line welcome message."
]
for question in questions:
    print("\nYou:", question)
    print("Agent:", agent(question))
    print("\nChallenge completed!")