infile = open("lab14_4.txt", "r")
search_word = input("단어 입력: ")

word_dic = {}

for line in infile:
    words = line.split() #단어로 분리 
    for word in words: #각 단어에 대해 루프 
        word = word.lower() #대소문자 구분을 없애기 위해 소문자로 변환
        word = word.strip(",.") #문장부호 제거 
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

# 사용자가 입력한 단어의 빈도 확인 (대소문자 구분)
count = word_dic.get(search_word, 0)

print(f"{search_word} 빈도: {count}")

infile.close()