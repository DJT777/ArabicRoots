import codecs
with codecs.open("hans-wehr.txt", "r", encoding='utf8') as f:
    text = f.read()
with codecs.open("text.txt", 'w', encoding='utf8') as f:
    f.write(text)
