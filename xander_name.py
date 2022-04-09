def optional_greeter(name):
    if name.startswith('X'):
        print("We don't greet people with weird names :p")
        pass
    else:
        print('Hi there, ', name)

optional_greeter('xander')