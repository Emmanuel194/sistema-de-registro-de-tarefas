from flask import Flask
from app.routes import routes

app = Flask(__name__)

app.register_blueprint(routes)

@app.route("/")
def home():
    return "Bem-vindo ao registro de tarefas!"

if __name__ == "__main__":
    app.run(debug=True)
