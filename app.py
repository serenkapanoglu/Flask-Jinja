from flask import Flask, request, render_template, redirect
from random import randint, choice, sample

#from flask_debugtoolbar import DebugToolbarExtension



#debug= DebugToolbarExtension(app)
app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/hello')
def say_hello(): 
    return render_template("hello.html")



@app.route('/form')
def show_form():
    return render_template("form.html")

COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "Pythonic"]

MAJORS = ["computer science", "history", "math", "archt", "chemical engineering"]

@app.route('/greet')
def get_greeting():
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=nice_thing)



@app.route('/lucky')
def lucky_number():
    num = randint(1,10)
    iltifat= choice(COMPLIMENTS)
    bolum= choice(MAJORS)
    return render_template('lucky.html', msg="You are so lucky",lucky_num=num, iltifatlar=iltifat, majors=bolum)

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result= request.form
        return render_template("result.html", result=result)
    
@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template('spell_word.html', word=word)


@app.route('/form2')
def show_form_2():
    return render_template("form_2.html")


@app.route('/greet2')
def get_greeting_2():
    username= request.args["username"]
    wants=request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS,3)
    return render_template("greet2.html", username=username, want_compliments=wants, compliments=nice_things)
    
    

    

@app.route('/story')
def tell_story():
    place = request.args.get("place")
    noun = request.args.get("noun")
    verb = request.args.get("verb")
    adj = request.args.get("adj")
    plural = request.args.get("plural")
    return render_template("story.html")

@app.route('/hikaye')
def tell_hikaye():
    place = request.args.get("place")
    noun = request.args.get("noun")
    verb = request.args.get("verb")
    adj = request.args.get("adj")
    plural = request.args.get("plural")
    story=f"Once upon a time in a long-ago {place}, there lived a large {adj} {noun}. It loved to {verb} {plural}."
    return render_template("hikaye.html", story=story)


@app.route('/form3')
def show_form_3():
    return render_template("form3.html")

@app.route('/page')
def show_page():
    isim=request.args["isim"]
    return render_template("page.html", isim=isim)
    
