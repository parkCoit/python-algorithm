class Solution:
    def solution(self, money):
        title = " ### 화폐교환 ### "
        arster = "*"*30
        answer = f" 요청금액 : {money} 원  "
        count = 0
        unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
        for i in unit:
            count = money // i
            money = money % i 
            print(f'{i}원짜리 {count}개 ')
        return f" {title}  \n {arster} \n {answer} "
        

if __name__=="__main__":
    solution = Solution()
    money = int(input( " 금액 : "))
    print(solution.solution(money))

