print('''
*************************
*************************
      PALINDROME
*************************
*************************
''')
word = input("Enter word: ")
print()
convert = word
palindrome_checker = ''
for i in convert:
    palindrome_checker = i + palindrome_checker
print()
print(f'Original word: {convert}')
print(f'Reverse word: {palindrome_checker}')
if palindrome_checker == convert:
    print(f"{word} is a palindrome")
else:
    print(f'{word} is not a plaindrome')
