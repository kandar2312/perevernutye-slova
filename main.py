def reverse_word(word):
    return word[::-1]


def normalize(text):
    return text.strip().lower()


def check_word(answer,word):
    if normalize(answer) == normalize(word):
        return True
    else:
        return False


def read_choice(prompt,allowed):
    choice= input(prompt).strip()

    while choice not in allowed:
        print("Неверный выбор.Попробуйте еще раз.")
        choice= input(prompt).strip()

    return choice


def show_rules():
    print()
    print("Правила игры:")
    print("Нужно угадать 5 перевёрнутых слов.")
    print("На каждое слово даётся одна попытка.")
    print("Чтобы победить, нужно угадать 4 слова.")
    print()


def play_game():
    words = ["Алматы","колледж","робот","экран","тест"]

    score = 0

    for word in words:
        print()
        print("Перевёрнутое слово:", reverse_word(word))

        answer = input("Введите слово: ")

        if check_word(answer,word):
           print("Правильно!")
           score = score+1
        else:
          print("Неправильно!")
          print("Правильный ответ: ",word)

    print()
    print("Ваш результат", score ,"из 5")

    if score >= 4:
        print("Победа")
    else:
        print("Поражение")

def main():
    choice= ""

    while choice != "0":
        print()
        print("ИГРА «ПЕРЕВЁРНУТЫЕ СЛОВА»")
        print("1 - Правила")
        print("2 - Начать игру")
        print("0-Выход")

        choice=read_choice("Выберите действие: ",["0","1", "2"])

        if choice == "1":
            show_rules()
        elif choice == "2":
             play_game()
        elif choice == "0":
             print("До свидания!")
main()
