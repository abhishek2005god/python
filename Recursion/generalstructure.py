#This is the general structure of a recursive function

def function(n):
    if n == 0:
        return
    print(n)
    function(n - 1) # Function calls itself