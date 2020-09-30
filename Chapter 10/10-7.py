print("please input 2 numbers, I'll add them together and show the result.")
while True:
    first_number = input("First number: ")
    second_number = input("Second number: ")

    try:
        answer = int(first_number)+int(second_number)
    except ValueError:
        print("please input only numbers.")
    else:
        print(f"the answer is {answer}")
    
