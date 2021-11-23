ja_list = []
en_list  = []

with open('english_word.csv','r',encoding='utf-8')as f:
    words_text = f.readlines()
    for word_text in words_text:
        word = word_text.split(',')
        en = word[0]
        en_list.append(en)
        ja = word[1]
        ja = ja.rstrip('\n')
        ja_list.append(ja)

words_dict = dict(zip(ja_list,en_list))
search = str(input('英語翻訳します>>'))
print(words_dict[search])