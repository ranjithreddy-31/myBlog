from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Ranjith Reddy Gaddam',
        'title': 'First Post',
        'content': 'First Post content',
        'date': '05 Feb, 2024'
    },
    {
        'author': 'John Cena',
        'title': 'Second Post',
        'content': 'Second Post content',
        'date': '05 Feb, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = "title")

if __name__ == '__main__':
    app.run(port = 8000,debug = True)