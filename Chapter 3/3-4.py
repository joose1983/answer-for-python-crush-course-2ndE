guest_list=['jackie','robert','jenny']
for index in guest_list:
    print(index,", let's have dinner together")
print(guest_list[0],", cannot join this dinner")
guest_list[0]='tom'
for index in guest_list:
    print(index.title(),", let's have dinner together")
print("I found a bigger table")
guest_list.insert(0,'johnny')
guest_list.insert(2,'catherine')
guest_list.append('rose')
for index in guest_list:
    print(index.title(),", let's have dinner together")
print("sorry I can only invite two guests")
for number in range(len(guest_list)):
    if(len(guest_list)>2):
        guest_list.pop()        
for index in guest_list:
    print(index.title(),", let's have dinner together")
for number in range(len(guest_list)):
    print(number)
    del guest_list[0]
print("now our guest list is:",guest_list)                    
