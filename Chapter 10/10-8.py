def show_file_content(filename):

    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"the file {filename} cannot be found!")
    else:
        print(f"the file {filename} contents are:")
        print(contents)

show_file_content('cats.txt')
show_file_content('dogs.txt')
show_file_content('noname.txt')

