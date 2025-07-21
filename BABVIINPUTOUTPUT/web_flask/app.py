from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama = request.form["nama"]
        nim = request.form["nim"]
        prodi = request.form["prodi"]
        return render_template("hasil.html", nama=nama, nim=nim, prodi=prodi)
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
