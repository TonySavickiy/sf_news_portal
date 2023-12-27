from django import template


register = template.Library()



DIRTY_WORDS = {
    'д': ['дебил', 'дрянь', 'даун', 'долбоёб'],
    'и': ['идиот', 'изверг'],
    'м': ['мудак','мудила', 'морковканюх'],
    'р': ['редиска', 'роботоед'],
    'х': ['хуй', 'хуёвый', 'хуёвая']
}

@register.filter()
def censor(textnews):
    word_list = textnews.split(' ')
    for idx, value in enumerate(word_list):
        if value:
            if value[0].lower() in DIRTY_WORDS.keys():
                for el in DIRTY_WORDS[value[0].lower()]:
                    if el in value.lower():
                        corrected = value[0] + '*' * (len(el)-1) + value[len(el):] #Меняем слово на букву + звёздочки
                        word_list[idx] = corrected #Заменяем в исходном тексте на отформатированный вариант

    return ' '.join(word_list)