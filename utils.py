#Здесь лежат функции
# получаем список слов с внешенего ресурса
data = [{
    "word":"питон",
    "subwords":[
        "ион", "иот", "нит", "нот", "нпо", "нто", "они", "опт", "пот", "тип", "тон", "топ", "пино", "пион", "пони", "понт", "поти"
]},
{
    "word":"барон",
    "subwords":[
        "аон", "бан", "бар", "боа", "бор", "наб", "оба", "обр", "она", "бора", "арон", "нора", "роба", "рона", "барон", "боран"
]},
{
    "word":"строка",
    "subwords":[
        "акр", "акт", "арк", "арт", "аск", "атс", "кар", "кат", "кот", "кто", "ока", "окр", "ора",
        "орс", "орт", "оса", "оск", "ост", "отк", "рак", "рао", "рок", "рос", "рот", "рта", "сак",
        "сок", "сор", "сот", "ста", "сто", "стр", "так", "тар", "ток", "тор", "карт", "коат", "кора",
        "корт", "коса", "крат", "крот", "окат", "орск", "раст", "роса", "рост", "рота", "сарт", "скат",
        "скот", "сокр", "сорт", "сота", "сотр", "срок", "сток", "таро", "тора", "торс", "тоса", "трак",
        "трас", "трок", "трос", "артос", "карст", "коста", "кроат", "окрас", "оскар", "скора", "сотка",
        "стора", "тоска", "кастор", "костра", "сократ", "торакс"

]}
]

#Создаст экземпляр класс Basic_word
from basic_word import Basic_word


def load_random_word():
    data_keys = data.keys()
    for key in data_keys:
        print(key)
        #return random.choice(data)

    return Basic_word(data["word"], data["subwords"])





    #Получит список слов с внешего ресурса
    #выберет случайное слова
