rivers={'nile' : 'egypt' , 'yellow river' : 'China' , 'Seine' : 'France' , 'Longriver': 'China'}
for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}")
for key in rivers.keys():
    print(key.title())
for value in set(rivers.values()):
    print(value.title())
