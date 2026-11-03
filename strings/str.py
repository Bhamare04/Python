#find and replace the email address in a text using regex
# import re

# text = "Please contact us at support@example.com or sales@example.com for more information."
# email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# new_text = re.sub(email_pattern, 'XXXXXX', text)
# print(new_text)

# def str_vowels(s):
#     vowels = "aeiouAEIOU"
#     count =0
#     for char in s:
#         if char in vowels:
#             count+=1
#             return count

# str_vowels("Hello World")


#reverse the words in a string
def reverse_words(s):
    words = s.split()
    reversed_words = " ".join(reversed(words))
    return reversed_words

reverse_words("Hello World")