"""
Caesar Cipher exercise inspired by freeCodeCamp prompts.
Focus: string manipulation, validation, and translation tables.
"""

def caesar(text, shift, encrypt=True):
    '''
    A flexible Caesar cipher function.
    If encrypt=True → text is encrypted
    If encrypt=False → text is decrypted (shift automatically reverses)
    '''

    # - - - VALIDATION - - -
    # Ensure the shift parameter is a whole number (int).
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    
    # Ensure shift is within a useful range.
    # A shift of 0 or 26+ would produce the original text unchanged.
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'
    # - - - BASE ALPHABET - - -
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # - - - DIRECTION CONTROL - - -
    # If decrypting, reverse the direction of the shift.
    # Example: encrypt shift=3 becomes decrypt shift=-3
    if not encrypt:
        shift = - shift

    # - - - CREATE SHIFTED ALPHABET - - - 
    # Slicing rotates the alphabet.
    # Example: shift=3 → 'def...abc'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # - - - CREATE TRANSLATION MAP - - - 
    # maketrans maps each letter to its shifted version.
    # We duplicate for uppercase letters so case is preserved.
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet +
    shifted_alphabet.upper()
      )
    
    # - - - PERFORM ENCRYPTION OR DECRYPTION - - -
    # translate() replaces each character using the translation map.
    # Non-letter characters remain unchanged (spaces, punct., numbers).
    return text.translate(translation_table)       
   
# - - - FRIENDLY WRAPPER FUNCTIONS - - - 
def encrypt(text, shift):
    # Encrypts text using the Caesar cipher.
    return caesar(text, shift)
def decrypt(text, shift):
    # Decrypts text by reversing the shift.
    return caesar(text, shift, encrypt=False)

# - - - EXAMPLE RUN 1 - - - 
encrypted_text = caesar ('freeCodeCamp', 3)
print(encrypted_text) 	# Example output: iuhhhFrghFdps
# - - - EXAMPLE RUN 2 - - -
encrypted_text =  'Pbhentr vf sbhaq va hayvxryl cynprf.'
print(encrypted_text)	# Pbhentr vf sbhaq va hayvxryl cynprf.
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)	# Courage is found in unlikely places.
