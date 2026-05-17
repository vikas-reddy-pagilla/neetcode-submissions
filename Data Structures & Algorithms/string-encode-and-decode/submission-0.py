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
        for char in s:
            word += char
            if char == '#': #string end
                chars_list = word.split(",")
                decoded_string = ''
                for value in chars_list:
                    if value == '#':
                        break
                    decoded_string += chr(int(value))
                decoded_strs.append(decoded_string)
                word = ''
            
        return decoded_strs
            

