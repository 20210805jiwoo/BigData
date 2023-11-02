input_file_name = input("입력 파일 이름: ")
output_file_name = input("출력 파일 이름: ")

with open(input_file_name, "r") as data_file:
    data_lines = data_file.readlines()

# 실수값 리스트로 변환
num = [float(line.strip()) for line in data_lines]

total = sum(num)
avg = total / len(num)

# 결과 출력 파일에 저장
with open(output_file_name, "w", encoding = "utf-8") as output_file:
    output_file.write(f"합계={total}\n평균={avg}")
