string1 = input("Please enter your string : ")

string2 = ''

for i in string1:
    string2 = i + string2
    
print("\nOriginal string = ", string1)
print("Reverse string  = ", string2)