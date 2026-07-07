# Normal function (no decorator)
def hello():
    print("Hello")
    
hello()

# Now we add “extra behavior manually
def hello():
    print("Hello")

print("Start")
hello()
print("End")

#Instead of above, we can use a decorator to add extra behavior to the function without modifying it.
# Decorator
def wrapper(func):
    def inner():
        print("Start")
        func()
        print("End")
    return inner
@wrapper
def hello():
    print("Hello")

hello()