filename = 'response.txt'
with open(filename,'a') as file_object:
    while True:
        response=input("please tell us why you like programming: ")
        file_object.write(response + '\n')
    
