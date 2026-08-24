def str_functions(str):
    # print("Length of the string:", len(str))

    # print("String in uppercase:", str.upper())
    # print("String in lowercase:", str.lower())
    # print("String in Reverse:", str[::-1])
    if(str == str[::-1]):
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")


    for i in str:
        count =0
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            count += 1
            print(count)

str = input("Enter a string: ")
str_functions(str)