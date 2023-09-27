def BMI(height, weight):
    return weight / height ** 2
    
def result_print(result):
    if result < 18.5:
        key = "저체중"
    elif 18.5 <= result <= 22.9:
        key = "정상"
    elif 23 <= result <= 24.9:
        key = "과체중"
    elif 25 <= result <= 29.9:
        key = "경도비만"
    else:
        key = "고도비만"
        
    print(f"당신의 체지방지수는 {result:.2f}입니다.")
    print(f"당신은 {key}입니다.")

h = float(input("키를 m단위로 입력: "))
w = float(input("몸무게를 kg단위로 입력: "))

result = BMI(h, w)
result_print(result)