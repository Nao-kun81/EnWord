from logging import debug
from flask import Flask
from flask import render_template,redirect,request
import random

#ーーーーーーーーーーー辞書ーーーーーーーーーーー
#csvファイルから英単語と日本語訳をそれぞれのリストに分ける
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

words_dict = dict(zip(en_list,ja_list))
#英単語 & 日本語訳
correct_answer = random.choice(en_list)
question_word = words_dict[correct_answer]

EnWord_image = 'media/EnWord.png'

#ーーーーーーーーーーーflaskーーーーーーーーーーー
app = Flask(__name__)

user_answer=''

@app.route('/', methods=['GET','POST'])
def index():
    #POST
    global user_answer
    global correct_answer
    global question_word
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == correct_answer:
            user_answer = 'True'
            return redirect('/answer')

        else:
            user_answer = 'False'
            return redirect('/answer')
    #GET
    else:
        correct_answer = random.choice(en_list)
        question_word = words_dict[correct_answer]
        return render_template('home.html',question_word=question_word)

@app.route('/answer', methods=['GET','POST'])
def answer():
    global user_answer
    #POST
    if request.method == 'POST':
        return redirect('/')

    #GET
    else:
        if user_answer == 'True':
            return render_template('answer.html', check='正解!!', correct_answer=correct_answer)

        else:
            return render_template('answer.html', check='不正解..',correct_answer=correct_answer)


if __name__ == '__main__':
    app.run(debug=True)
        
#   Powershell
#   $env:FLASK_APP = "app"
#   $env:FLASK_ENV = "development"

#   CMD
#   set FLASK_APP=app
#   set FLASK_ENV=development

#   flask run