from flask import Flask, render_template, url_for
app = Flask(__name__)


def random_surge():
    import random
    with open('surges.txt', 'r') as f:
        lines = f.readlines()
    
    return random.choice(lines)

@app.route("/")
@app.route("/home")
def home():
    return render_template('base.html', surge=random_surge())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #app.run(host='0.0.0.0', port=80)