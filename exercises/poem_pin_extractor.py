"""
Extract numeric codes from poems based on word position logic.

For each poem, the function analyzes each line and derices a numeric value
using the relationship between line position and word count.
Fallback values are applied when a line does not contain enough words.
"""
# Define a function that extracts data from the input poems
def pin_extractor(poems):

    secret_codes = []

    # Process each poem in the input list
    for poem in poems:

        # Create an empty string to store extracted values
        secret_code = ''

        # split('\n') returns a list of substrings split at each newline character
        lines = poem.split('\n')

        # Iterate through each line while tracking its position
        for line_index, line in enumerate(lines):
            # Split the current line into a list of words using whitespace (default)
            words = line.split()

            # Only proceed if the current line has enough words for this index
            if len(words) > line_index:
                # Append the length of the selected word to the secret code
                secret_code += str(len(words[line_index]))

            else:
                # Append a fallback value when the current line has no word at this index
                secret_code += '0'

        # Store the extracted code for this poem
        secret_codes.append(secret_code)

    return secret_codes

poem = "Stars and the moon\nshine in the sky\nwhite and bright\nuntil the end of the night"
poem2 = "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow"
poem3 = "There\nonce\nwas\na\ndragon"

# Call the function using a LIST [] of poems as the argument
print(pin_extractor([poem, poem2, poem3]))