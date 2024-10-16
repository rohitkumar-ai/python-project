def count_vowels():
    # Take input from the user
    text = input("Enter a sentence or word: ").lower()

    # Define vowels
    vowels = "aeiou"

    # Initialize vowel count
    vowel_count = 0

    # Loop through each character in the text
    for char in text:
        if char in vowels:
            vowel_count += 1

    # Print the result
    print(f"Number of vowels: {vowel_count}")

# Call the function
count_vowels()
