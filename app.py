from flask import Flask, render_template


app = Flask(__name__)


#Основная страница
@app.route("/")
def about():
    return render_template("about.html")


#Запускаем локальный сервер
if __name__ == "__main__":
      app.run(debug=True)
