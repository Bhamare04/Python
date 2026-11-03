a = int(input("Enter the number of terms: "))
a1 = 0
a2 = 1
count =0
while count < a:
    print(a1)
    nth = a1 + a2
    a1 = a2
    a2 = nth
    count += 1
   