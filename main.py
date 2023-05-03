from flask import Flask, render_template

app = Flask(__name__)

listGames = [
    {
        "name": "Dark souls 3",
        "price": 49.99,
        "image_url": "img/darkSouls3.jpg"
    },
    {
        "name": "Doom eternal",
        "price": 34.99,
        "image_url": "img/doomEternal.jpg"
    },
    {
        "name": "Hollow Knight: Silksong",
        "price": 14.99,
        "image_url": "img/silksong.jpeg"
    },
    {
        "name": "The Legend of Zelda: Tears of The Kingdom",
        "price": 24.99,
        "image_url": "img/zelda.jpg"
    }
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shopping')
def shopping():
    return render_template('shopping.html', listGames=listGames)

@app.route('/contact')
def gaming():
    return render_template('contact.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
