#Основной файл приложения
import random
from utils import load_random_word
from player import Player


def get_word():
    return random.choice(data)
def main():

    main_word = load_random_word()
    word = main_word.data #Вытаскиваем из слова

    wordcaunt = main_word.count_subword() # Считает количество слов
    print(f"составьте {wordcaunt} слов из слова {word} ")

    while True:
    #Получаем данные пользователя
        user_input = input("Велите слово")
        if main_word.correct_word(user_input):
            print("слово есть ")
        else:
            print("Слова нет ")

main()