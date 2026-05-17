class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        result = {}
        for string in strs:
            freq_key= [0]*26
            for i in string:
                freq_key[ord(i) - ord('a')] += 1
            freq = tuple(freq_key)

            if freq in result:
                result[freq].append(string)
            else:
                result[freq] = []
                result[freq].append(string)
        return list(result.values())

        # result={}
        # for ever string 
        #     freq={}
        #     freq(str)
        #     if result.find(freq(str)) == found
        #     result[freq(str)].append(str)
        #     else:
        #         result[freq(str)]=[]
        #         result[freq(str)].append(str)


        