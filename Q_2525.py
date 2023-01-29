class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        v = length*width*height
        cat1=""
        cat2=""
        if(length>=10**4 or width>=10**4 or height>=10**4 or v>=10**9):
            cat1 = "bulky"
        if(mass>=100):
            cat2 = "heavy"
        if(cat1=="bulky" and cat2=="heavy"):
            return("Both")
        elif(cat1=="bulky" and cat2!="heavy"):
            return("Bulky")
        elif(cat1!="bulky" and cat2=="heavy"):
            return("Heavy")
        else:
            return("Neither")