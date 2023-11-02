import random

def choose_word():
    with open("hangman.txt", "r") as file:
        words = file.read().splitlines()
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '*' for letter in word)

def hangman():
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts = 10

    while '*' in display_word(word_to_guess, guessed_letters) and attempts > 0:
        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        guess = input("\n단어를 추측하시오: ").lower()

        if guess in guessed_letters:
            print("이미 추측한 글자입니다.")
            continue

        guessed_letters.add(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print(f"틀렸음! \n{attempts} 기회가 남았음!")

    print(f"사용자 승리" if '*' not in display_word(word_to_guess, guessed_letters) else f"패배! 정답은 {word_to_guess}")

hangman()
