# 989. Add to Array-Form of Integer
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        str_num = ""
        for ele in num:
            str_num+=str(ele)
        res = str(int(str_num)+k)
        res_list=[]
        for i in res:
            res_list.append(int(i))
        return(res_list)