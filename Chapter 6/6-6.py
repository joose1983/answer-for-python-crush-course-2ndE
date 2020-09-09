people_list=['jackie' , 'tom' , 'robert' , 'rose' , 'alice']
favorite_languages={'jackie':'c', 'rose':'python'}
for name in people_list:
    if name in favorite_languages.keys():
        print(f"{name} thnk you for responding")
    else:
        print(f"{name} please take the pool!")
