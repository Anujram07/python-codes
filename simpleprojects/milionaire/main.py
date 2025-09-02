questions = [
    ["Who is Jhonny Sins?", "Plumber", "Electrician", "Astronaut", "Teacher", 2],
    ["What is the capital of Pakistan?", "Sanatan puri", "Islamabad", "Karachi", "Delhi", 2],
    ["Who is the most successful captain of Indian Cricket captain?", "Thala", "Dada", "Kapil", "Rohit", 1],
    ["Who is the most successful Indian batsman?", "Thala", "Kohli", "Kapil", "Rohit", 2],
    ["Who is the most successful Bowler?", "Thala", "Bumrah", "Kapil", "Rohit", 2],
    ["Who is the batsman to hit 6 sixes in an over?", "Thala", "Dada", "Yuvraj", "Rohit", 3]
]


dhanraashi = [1000,10000,500000,100000,500000,1000000]
# sum = 0
i = 0
for question in questions:

    print("\n" + question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    # input from user
    a = int(input("Enter your answer (1/2/3/4): "))

    if question[5] == a:
        print("✅ Sahi Jawab! Kya baat hai 🎉")
    else:
        print(f"❌ Galat Jawab! Sahi answer hai: {question[question[5]]}")
        break

    print(f"Hey You won {dhanraashi[i]}")
    i += 1


# print("Saat crorreeeee")