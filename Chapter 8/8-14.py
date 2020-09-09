def make_car(manufacturer, model, **args):
    args['manufacturer']=manufacturer
    args['model']=model
    return args

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

