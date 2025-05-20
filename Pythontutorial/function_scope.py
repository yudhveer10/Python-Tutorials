def sum(a,b):
    c = a + b 
    #a and b are local variable.
    z = 1 # It creates a local variable
    print (z)
    return c

z = 8 #z is a global variable
print(sum(4,6))
print(z)