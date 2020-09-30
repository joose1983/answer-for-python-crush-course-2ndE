"""message.replace('dog', 'cat') will not change the message itself, but will return a replaced new string instead."""

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    new_line=line.replace('Python','C')
    print(new_line.strip())

