from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Halo, ini halaman utama!"

if __name__ == '__main__':
    app.run(debug=True)
