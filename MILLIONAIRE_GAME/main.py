questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],
    ["What is the capital of India?", "Mumbai", "Kolkata", "New Delhi", "Chennai", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    ["Who wrote 'Harry Potter'?", "J.K. Rowling", "C.S. Lewis", "Mark Twain", "Jane Austen", 1],
    ["What is the currency of Japan?", "Yen", "Dollar", "Rupee", "Euro", 1],
    ["Which animal is known as the King of Jungle?", "Lion", "Tiger", "Elephant", "Bear", 1],
    ["Who painted the Mona Lisa?", "Leonardo da Vinci", "Pablo Picasso", "Vincent Van Gogh", "Claude Monet", 1],
    ["What is the largest ocean in the world?", "Atlantic", "Indian", "Arctic", "Pacific", 4],
    ["Which gas do plants absorb from the atmosphere?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2],
    ["Who is known as the Father of Computers?", "Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs", 1],
    ["Which Indian city is known as the Pink City?", "Jaipur", "Udaipur", "Jodhpur", "Delhi", 1],
    ["What is H2O commonly known as?", "Salt", "Water", "Oxygen", "Hydrogen", 2],
    ["Who discovered gravity?", "Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla", 2],
    ["Which is the smallest continent by area?", "Australia", "Europe", "Antarctica", "South America", 1],
    ["Which country is called the Land of Rising Sun?", "China", "Japan", "Thailand", "South Korea", 2],
]

prizes = [
    1000,
    2000,
    3000,
    5000,
    10000,
    20000,
    40000,
    80000,
    160000,
    320000,
    640000,
    1250000,
    2500000,
    5000000,
    10000000
]

total = 0
i = 0

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    while True:
        try:
            a = int(input("Enter your answer (1 for a, 2 for b, 3 for c, 4 for d): "))
            if a not in [1, 2, 3, 4]:
                print("Enter a number between 1 and 4!")
                continue

            if question[5] == a:
                total += prizes[i]
                print(f"Correct Answer! You won {total}\n")
                break
            else:
                print(f"Incorrect, the correct answer was {question[question[5]]}")
                print(f"You'll go back with {total}")
                print("Better luck next time!")
                exit()
        except ValueError:
            print("Enter a valid number!")

    i += 1
