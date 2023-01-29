#1207. Count number of unique occurences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ=dict()
        for ele in arr:
            occ[ele]=0 #initialization
        for ele in arr:
            occ[ele]+=1
        occ_val = list(occ.values())
        if(len(occ_val)==len(set((occ_val)))):
            return True
        else:
            return False