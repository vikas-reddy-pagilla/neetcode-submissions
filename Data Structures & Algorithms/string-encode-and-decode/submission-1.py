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
        word = ''
        letter = ''
        for char in s:
            if char != '#' and char != ',':
                letter += char
            if char == ',':
                word += chr(int(letter))
                letter = ''
            if char == '#': #word end
                decoded_strs.append(word)
                word = ''
        return decoded_strs
            

