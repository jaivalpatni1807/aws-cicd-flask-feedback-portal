from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

feedback_list = []

@app.route('/')
def home():
    return render_template('index.html', feedback=feedback_list)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        user_feedback = request.form.get('feedback')
        if user_feedback:
            feedback_list.append(user_feedback)
        return redirect(url_for('home'))
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
