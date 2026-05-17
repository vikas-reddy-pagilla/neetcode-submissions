class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            for char in string:
                encoded_string += str(ord(char))
                encoded_string += ','
            encoded_string += '#'
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        current_word_chars = []
        current_letter_digits = []
        
        for char in s:
            if char == ',':
                # Convert the collected digits back to a character efficiently
                ascii_val = int("".join(current_letter_digits))
                current_word_chars.append(chr(ascii_val))
                current_letter_digits = [] # Clear for next letter
            elif char == '#':
                # End of a word block reached
                decoded_strs.append("".join(current_word_chars))
                current_word_chars = [] # Clear for next word
            else:
                # Accumulate digits for the current character code
                current_letter_digits.append(char)
                
        return decoded_strs
