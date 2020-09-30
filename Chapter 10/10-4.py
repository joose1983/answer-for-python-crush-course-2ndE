while True:
    guest_name = input("please input your full name: ")
    print(f"{guest_name}, Welcome to the Python world!")
    guest_name = guest_name + '\n'
    with open('guest_book.txt','a') as file_object:
        file_object.write(guest_name)
    
    
