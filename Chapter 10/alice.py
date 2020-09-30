filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"File {filename} not found.")

else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
    
    
    
