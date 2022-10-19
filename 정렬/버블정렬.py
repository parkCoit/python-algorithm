import random


class Solution:
    def solution(self):
        keys =['1st', '2nd', '3rd', '4th', '5th']  #입력
        dc = {}
        print(' ### 버블정렬 ### ')
        print( "*"*30 )
        for i in keys:  #정렬
            dc[i] = random.randint( 1, 11 )
        
        for k, v in dc.items():  #출력
            print( f' {k} : {v} ' )
        print( "*"*30 )

if __name__=="__main__":
    solution = Solution()
    solution.solution()