Number = int(input("\nPlease Enter the Range : "))
even=0
odd=0
for i in range(1,Number+1):
    print(i, end=" , ")
    if i%2==0:
        even+=1 
    else:
        odd+=1
print('\nEven count numbers in series is',even)
print('Odd count numbers in series is',odd)