# Simple quiz program to ask the user about the capitals of European countries
def quiz(question, capital):
    # Ask the user the question
    answer = input(question + " ")
    # Check if the answer is correct (ignoring capitalization)
    if answer.lower() == capital.lower():
        print("Well Done!")
    else:
        print("Ooops! The correct answer is " + capital + ".")
# dictionary of countries and their capitals
capitals = [
    ("What is the capital of France?", "Paris"),
    ("What is the capital of Germany?", "Berlin"),
    ("What is the capital of Italy?", "Rome"),
    ("What is the capital of Spain?", "Madrid"),
    ("What is the capital of Portugal?", "Lisbon"),
    ("What is the capital of Belgium?", "Brussels"),
    ("What is the capital of Netherlands?", "Amsterdam"),
    ("What is the capital of Austria?", "Vienna"),
    ("What is the capital of Greece?", "Athens"),
    ("What is the capital of Sweden?", "Stockholm")
]
# Loop through each question and ask the user
# for the capital of the country:
for question, capital in capitals:
    quiz(question, capital)
# End of the quiz
print("Quiz complete!")
# End of the program
print("Thank you for playing!")
