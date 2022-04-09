def welcome(name='learner', location='this tutorial'):
    print("Hi", name, "welcome to", location)

welcome()
# Hi learner welcome to this tutorial

welcome(name='John')
# Hi John welcome to this tutorial

welcome(location='this epic tutorial')
# Hi learner welcome to this epic tutorial

welcome(name='John', location='this epic tutorial')
#Hi John welcome to this epic tutorial

welcome('John', 'this epic tutorial')
#Hi John welcome to this epic tutorial