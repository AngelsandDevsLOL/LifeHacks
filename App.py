from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Add more routes for other pages if necessary

if __name__ == '__main__':
    app.run(debug=True)

