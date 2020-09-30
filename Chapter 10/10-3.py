guest_name = input("please input your full name here: ")
filename = "guest.txt"
with open(filename,'a') as file_object:
    file_object.write(guest_name)
