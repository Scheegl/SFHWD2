from django import template

register = template.Library()

CENSOR_WORDS = ('манга',)

@register.filter()
def censor_text(text):
    for word in text.split():
        if word.lower() in CENSOR_WORDS:
            if word.lower() in CENSOR_WORDS:
                text = text.replace(word, f"{word[0]}{'*' * (len(word) -1)}")
    return text

@register.filter()
def censor_title(title):
    for word in title.split():
        if word.lower() in CENSOR_WORDS:
            if word.lower() in CENSOR_WORDS:
                title = title.replace(word, f"{word[0]}{'*' * (len(word) -1)}")
    return title