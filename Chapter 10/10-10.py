filename = 'Ireland in Travail.txt'
keyword='the'
keyword1='the '
num_keyword=0
num_keyword1=0
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"sorry, the file {filename} cannot be found.")
else:
   
    num_keyword=contents.lower().count(keyword)
    print(f"in file {filename}, the number of words '{keyword}' are: {num_keyword}")
    num_keyword1=contents.lower().count(keyword1)
    print(f"in file {filename}, the number of words '{keyword1}' are: {num_keyword1}")
