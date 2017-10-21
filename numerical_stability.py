
# Numerical stability
# assign a variable, x = 10^9
# add 10^-6 to x 10^6 times
# subtract 10^9 from x
# Ideally we must get 1
# the code below prints 0.9536...

x = 10**9
b = 10**-6
for i in range(0, 10**6):
    x += b
diff = x - 10**9
print(diff)

# OUTPUT -> 0.953674316406

# Changing 10^9 to 1, the error becomes very small

x = 1
b = 10**-6
for i in range (0,10**6):
    x = x + b
diff = x - 1
print(diff)

# OUTPUT -> 0.999999999918
