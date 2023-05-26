#Take a number
#Declare a temporary variable and initialize it with 0
#Find the last digit of the number
#Multiply the temporary variable by 10
#Add that last digit to the temporary variable
#Remove the last digit of the number.
#Repeat this process from 3 to 6 until the number becomes 0.3


n=int(input("Enter the integer"))
reverse=0
while (n>0):
    last_digit=n%10
    reverse=reverse*10+last_digit
    n=n//10
print("The reverse of a number:",reverse)
