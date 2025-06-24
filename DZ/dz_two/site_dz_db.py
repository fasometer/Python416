import sqlite3
import os
from flask import Flask, render_template, flash, request, g, abort
from DZ.dz_two.dz_database import FDataBase

# конфигурация
DATABASE = '/DZ/dz_two/flsk.db'
DEBUG = True
SECRET_KEY = '25ef16e3071ef238a2e0e3160f90185d990ffa5b'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "flsk.db")))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row  # обращатся по ключам как в славре
    return con


def create_db():  # только для запуска sql файла один раз
    db = connect_db()
    with app.open_resource("dz_sql_db.sql", "r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.get_menu())


@app.route("/project")
def project():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('project.html', menu=dbase.get_menu(),posts=dbase.get_post_anonce())


@app.route("/contact", methods=["POST", "GET"])
def contact():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        print(request.form)
    return render_template('contact.html', title='Связаться с нами', menu=dbase.get_menu())


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        if len(request.form["name"]) > 4 and len(request.form["post"]) > 10:
            res = dbase.add_post(request.form["name"], request.form["post"])
            if not res:
                flash("Ошибка добавления проекта", category="error")
            else:
                flash("Проект добавлен успешно", category="success")
        else:
            flash("Ошибка добавления проекта", category="error")

    return render_template('add_post.html', title='Добавить проект', menu=dbase.get_menu())


@app.route("/post/<int:id_post>")
def show_post(id_post):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.get_post(id_post)
    if not title:
        abort(404)
    return render_template('post.html', menu=dbase.get_menu(), title=title, post=post)


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template("page404.html", title="Страница не найдена", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()


if __name__ == '__main__':
    app.run()
