def check_character(char):
    if len(char) != 1 or not char.isalpha():
        return "INVALID CHARACTER INPUT"
    char = char.lower()
    if char in 'aeiou':
        return f"{char} is a vowel."
    else:
        return f"{char} is a consonant."
user_input = input("Enter a single character: ")
result = check_character(user_input)
print(result)
