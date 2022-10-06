"""
평균
90이상은 A학점
80이상은 B학점
70이상은 C학점
60이상은 D학점
50이상은 E학점
그 이하는 F학점
"""
class Solution:
    def solution(self, a, b, c):
        title = " ### 성적표 ### "
        total = a + b + c
        avg = round(total / 3, 1)        
        if avg >= 90:
            grade = "A학점"
        elif avg <= 80:
            grade = "B학점"
        elif avg <= 70:
            grade = "C학점"
        elif avg <= 60:
            grade = "D학점"
        elif avg <= 50:
            grade = "E학점"
        else:
            grade = "F학점"  
        return f"{title} \n  총점 : {total}, 평균: {avg} 학점: {grade}" 

if __name__ == "__main__":
    solution = Solution()
    a = int(input(' 국어: '))
    b = int(input(' 영어: '))
    c = int(input(' 수학: '))
    
    print(solution.solution(a, b, c))