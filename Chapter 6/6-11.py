cities={
    'nanjing':{'country':'gulou', 'population': '900m', 'fact': 'middle east of china'},
    'beijing':{'country':'xidan', 'population': '3000m', 'fact': 'north of china'},
    'shanghai':{'country':'xuehui', 'population': '4000m', 'fact': 'east of china'}
        }
for city, description in cities.items():
    print(f"{city}'s country is {description['country']}")
    print(f"it has a population of {description['population']}")
    print(f"it's basic of fact is: {description['fact']}")
    
