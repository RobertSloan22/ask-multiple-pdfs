from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_question = None
    if request.method == 'POST':
        user_question = request.form.get('user_question')
        # Handle the user's question here...
    return render_template('index.html', user_question=user_question)

if __name__ == '__main__':
    app.run(debug=True)
