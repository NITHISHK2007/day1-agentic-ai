fees = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}

question = input("You: ").lower()

if "ai202" in question and "fee" in question:
    print("Fee for AI202 is Rs.18,000")

elif "ds303" in question and "cs101" in question and "difference" in question:
    print("Difference is Rs.3,000")

elif "cs101" in question and "ai202" in question and "10%" in question:
    total = fees["CS101"] + fees["AI202"]
    after_scholarship = total * 0.90
    print("Total after 10% scholarship is Rs.", after_scholarship)

else:
    print("Sorry, I don't understand the question.")