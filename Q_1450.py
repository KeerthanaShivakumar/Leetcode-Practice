# 1450. Number of Students Doing Homework at a Given Time
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for i in range(len(startTime)):
            if(queryTime in range(startTime[i], (endTime[i]+1))):
                count+=1
        return count