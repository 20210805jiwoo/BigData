infile = open("num.txt", "r")

numbers = []
for line in infile:
    try:
        num = int(line)
        numbers.append(num)
    except ValueError:
        # ValueError가 발생하면 무시하고 계속 진행
        pass

infile.close()  

total = sum(numbers)
avg = total / len(numbers)

print(f"합은 {total}")
print(f"평균은 {avg}")

outfile = open("num.txt", "a") 

# 결과를 파일에 추가
outfile.write(f"\n합은 {total}\n평균은 {avg}")

outfile.close() 
