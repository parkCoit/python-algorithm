import random

class Solution:
    def solution(self):
        keys = [ '1st', '2nd' ,'3rd', '4th', '5th' ]
        dc = {}
        for i in keys:
            dc[i] = random.randint(0, 100)

        for k, v in dc.items():
            print( f' {k} : {v} ' )
        

if __name__=="__main__":
    solution = Solution()
    solution.solution()