input_file_name = input("입력 파일 이름 입력: ")
output_file_name = input("출력 파일 이름 입력: ")
delete_str = input("삭제할 문자열을 입력: ")

try:
    with open(input_file_name, "r") as infile:
        contents = infile.read()

    modified_content = contents.replace(delete_str, "")

    with open(output_file_name, "w") as outfile:
        outfile.write(modified_content)

    print("변경된 파일이 저장되었습니다.")
    
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")