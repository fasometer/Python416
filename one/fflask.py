from flask import Flask, render_template, request

app = Flask(__name__)

menu = [
    {'name': "Главная", "url": "index"},
    {'name': "О нас", "url": "about"},
    {'name': "Обратная связь", "url": "contact"}
]


@app.route("/")  # http://127.0.0.1:5000/
@app.route("/index")
def index():
    return render_template('index.html', title="Главная", menu=menu)


@app.route("/about")  # http://127.0.0.1:5000/about
def about():
    return render_template('about.html', title="О нас", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        print(request.form)
        print(request.form['username'])
    return render_template('contact.html', title="Обратная связь", menu=menu)


@app.route("/profile/<path:username>")  # http://127.0.0.1:5000/profile/admin
def profile(username):
    return f"Пользователь: {username}"  # динамические параметры в адресную строку


if __name__ == '__main__':
    app.run(debug=True)
