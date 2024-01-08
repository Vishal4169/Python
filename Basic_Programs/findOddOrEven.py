
def findOddOrEven(givenData): 
  if(givenData%2 == 0):
    print(givenData ,"is an Even Number")
  else:
    print(givenData , "is an Odd Number")


givenData = int(input("Enter the number"))

findOddOrEven(givenData)