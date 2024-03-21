name = 'This is an "example" with quotation marks'
stringLiteralOrScape = "This is an example for scaping or \"literals\'..."
lineBreak = "This is an example of line \n break"

# \n line break
# \b removes white space
# \f, \v prints symbols 
# \r removes all the previous text

print(name)
print(stringLiteralOrScape)
print(lineBreak)

num = 1
print(type(str(num)))

string = "This is an example of strings for substrings"
print(len(string))  # --> 54
print(string[2])    # --> i
print(string[0:12]) # --> This is an e  (T=0, e=11, x=12 omitted)
print(string[ :12]) # --> This is an e  (assumes 0)
print(string[11:18])   # --> example
print(string[-1])      # --> s  (reverse count)
print(string[-33:-26]) # --> example
print(string[0:-1]) # --> This is an example of strings for substring

# String Methods
'''
string.lower(), .upper(), .capitalize(), .title(), .swapcase()
'''
print("String method .title(): ", string.title())
print("String method .swapcase(): ", string.swapcase())

