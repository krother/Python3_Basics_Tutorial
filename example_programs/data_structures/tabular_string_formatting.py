	
# Example: String Formatting

apple = ('apple','Granny Smith','green')
banana = ('banana','Equador', 245)
orange = ('orange','Spain', 315.2)

print

# use a string function
print ", ".join(apple) 
print

# concatenate strings
s = banana[0] + " (" + banana[1] + "); weight: " + str(banana[2]) + "g\n" 
print s

# use string formatting
s = "\tfruit : %12s\n\torigin: %12s\n\tweight: %12.2fg\n"%orange
print s


