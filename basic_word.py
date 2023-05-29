#Здесь лежат класс слова


class Basic_word():
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    #Проверка введеного слова в списке допустимых подслов
    def correct_word(self, words):
        return words.lower() in self.subwords

    #подсчёт количества подслов
    def count_subword(self):
        return (len(self.subwords))

    def __repr__(self):
        return f"{self.word} содержит {len(self.subwords)} слов"

z = Basic_word("птион", "он")
