# Ask the user for input and a shift key
input_string = input("Enter the input string: ")
key = int(input("Enter the key (a number to shift letters): "))

# Initialize an empty string for the encrypted text
cipher = ""

# Check if the input contains numbers
if not any(char.isdigit() for char in input_string):
    for char in input_string:
        if char.isalpha():  # If the character is a letter
            if char.islower():  # If it's a lowercase letter
                shifted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
            cipher += shifted_char
        elif char == " ":
            cipher += "#"  # Replace spaces with "#"
        else:
            cipher += char  # Keep non-alphabet characters as they are

    # Print the encrypted text
    print(f"Encrypted Text: {cipher}")

    # Initialize an empty string for the decrypted text
    decrypted_text = ""

    for char in cipher:
        if char.isalpha():
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') - key) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
            decrypted_text += shifted_char
        elif char == "#":
            decrypted_text += " "  # Replace "#" with spaces
        else:
            decrypted_text += char

    # Print the decrypted text
    print(f"Decrypted Text: {decrypted_text}")

else:
    print("Error: Your input contains numbers.")

# Count the frequency of each character in the input
char_count = {}
total_alphabets = sum(1 for char in input_string if char.isalpha())

for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print character frequencies as percentages of total alphabets
for char, count in char_count.items():
    frequency_percentage = int((count / total_alphabets) * 100)
    print(f"{char}: {frequency_percentage}%")
