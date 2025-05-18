from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    mensagem = ""
    numero = request.form.get("secreto") or random.randint(1, 100)
    numero = int(numero)

    if request.method == "POST":
        dificuldade = request.form.get("dificuldade", "easy")
        tentativas = int(request.form.get("tentativas", 10))
        if tentativas == 10:
            tentativas = 10 if dificuldade == "easy" else 5

        palpite = int(request.form["palpite"])

        if palpite == numero:
            mensagem = f"🎉 You win! The number was: {numero}."
        else:
            tentativas -= 1
            if tentativas == 0:
                mensagem = f"💥 Game Over.  The number was: {numero}."
            elif palpite > numero:
                mensagem = f"📉 The number guessed is too high. You have {tentativas} attempts"
            else:
                mensagem = f"📈 The number guessed is too low. You have {tentativas} attempts"

        return render_template("index.html", mensagem=mensagem, tentativas=tentativas, secreto=numero, dificuldade=dificuldade)

    # primeira vez: GET
    return render_template("index.html", mensagem="", tentativas=10, secreto=numero, dificuldade="easy")

if __name__ == "__main__":
    app.run(debug=True)
