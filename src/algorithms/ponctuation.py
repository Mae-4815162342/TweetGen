from deepmultilingualpunctuation import PunctuationModel

def ponctuation(text):
    model = PunctuationModel()
    result = model.restore_punctuation(text)
    first = result[0].upper()
    result = first + result[1:]
    return result

print(ponctuation("hello i love potatoes and you"))
