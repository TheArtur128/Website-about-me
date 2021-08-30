from flask import Flask, render_template

#Создаём приложение
app = Flask(__name__)


#Основная страница
@app.route("/")
def about():
    return render_template("about.html")


#Другая страница
@app.route("/other")
def other():
    return render_template("other.html")


#Запускаем локальный сервер
if __name__ == "__main__":
      app.run(debug=True)
