def caesar(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char #알파벳 아니면 그대로 결과 문자열에 추가 
    return result

plaintext = "the language of truth is simple."

ciphertext = caesar(plaintext, 3)

print(f"평문: {plaintext}")
print(f"암호문: {ciphertext}")
