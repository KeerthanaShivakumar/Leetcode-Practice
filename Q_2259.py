# 2259. Remove Digit From Number to Maximize Result
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        #the number next to the leftmost occurrence must be maximum
        index=-1
        #find the index
        for i in range(len(number)-1):
            if((number[i]==digit) and (number[i]<number[i+1])):
                index=i
                break
        #if index not found, use the left most occurence
        if(index==-1):
            for i in range(len(number)-1, -1, -1):
                if(number[i]==digit):
                    index=i
                    break
        res=""#final answer
        for i in range(len(number)):
            if(i!=index): #to remove only one occurrence
                res = res+number[i]
        return res