import random
print("<< 덧셈 문제 연습 게임 >>")
print("------------------------")

correct_num = 0
i = 0

while correct_num < 5:
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    
    ans = int(input(f'{num1} + {num2} = '))
    i += 1

    if ans == num1+num2:
        print("맞았다.")
        correct_num += 1
    else:
        print("틀렸다.")

print("시도횟수: ", i)
    