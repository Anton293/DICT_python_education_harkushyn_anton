bot_name = "bot"
birth_year = "2050"

print(f"""
Hello! My name is {bot_name}.
I was created in {birth_year}.
    
Please, remind me your name.
""")

my_name = input("your name:")

print(f"What a great name you have, {my_name}!")
print("Let me guess your age.\n Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input("на 3:"))
remainder5 = int(input("на 5:"))
remainder7 = int(input("на 7:"))

your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {your_age}; that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
for i in range(int(input(">>>"))):
    print(f"{i}!")


print("Completed, have a nice day!")
#asked
print("""
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.
""")
for i in range(99):
    reply_test = int(input(">>>"))
    if reply_test == 2:
        print("Completed, have a nice day!")
        break
    else:
        print("Please, try again.")


print("Congratulations, have a nice day!")
