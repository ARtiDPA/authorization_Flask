from flask import Flask, render_template

app = Flask(__name__)


@app.route("/add")
def add_route():
    return render_template("add.html")


if __name__ == "__main__":
    app.run()
