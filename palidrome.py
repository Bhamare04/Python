a = int(input("Enter a number: "))
original = a
rev = 0

while a > 0:
    digit = a % 10
    rev = rev * 10 + digit
    a = a // 10

if rev == original:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")