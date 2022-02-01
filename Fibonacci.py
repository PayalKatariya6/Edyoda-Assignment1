Number = int(input("\nPlease Enter the Range : "))
i = 0
First_Value = 0
Second_Value = 1
           

while(i < Number):
           if(i <= 1):
                      Result = i
           else:
                      Result = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Result
           print(Result,end=" ")
           i = i + 1
