#Тут класс игрока
class Player():
    def __init__(self, name, words_used ):
        self.name = name
        self.words_used = words_used #Использованные слова
        words_used = []
    #Получение количества использованных слов
    def getting_used_word(self):
        return len(self.words_used)

    #Добавление в использовынные слова
    def adding_to_used(self,new_word):
        words_used.append(new_word)

    #Проверка использования данного слова до этого
    def check_word(self, word):
        return word in self.words_used

    def __repr__(self):
        return f"{self.name} угадал слова {(self.words_used)}"
