from flask import Flask, render_template, request

app = Flask(__name__)

menu = [
    {'name': "Главная", "url": "index"},
    {'name': "Наши проекты", "url": "project"},
    {'name': "Связаться с нами", "url": "contact"}
]


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='Главная', menu=menu)


@app.route("/project")
def project():
    return render_template('project.html', title='Наши проекты', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
