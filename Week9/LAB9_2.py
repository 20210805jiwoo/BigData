file_name = input("파일 이름을 입력하세요: ")

try:
    with open(file_name, "r") as file:
    contents = file.read()
        
    word_count = len(contents)
        
    print(f"파일 안에는 총 {word_count} 개의 글자가 있습니다.")

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
    