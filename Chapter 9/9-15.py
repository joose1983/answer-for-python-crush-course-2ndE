from random import sample

my_ticket="1234567890abcde"
flag=-1
count=0
while(flag==-1):
    winner=sample(my_ticket,4)
    winner="".join(winner)
    flag=my_ticket.find(winner)
    count+=1
    print(count)
print(f"my ticket is:{my_ticket}")
print(f"selected string is:{''.join(winner)}")
print(f"we tried {count} times to match the string!")




