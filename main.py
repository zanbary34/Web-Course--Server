from flask import Flask, redirect,render_template
app = Flask(__name__)
@app.route('/')
@app.route('/home')
def index_func():
    return render_template('Home.html')

@app.route('/contact')
def about_page():
    user_info = {'name': "Jack" ,"second_name": "Sparo"}
    degrees =  []
    hobbies =()
    return render_template('Contact.html',user_info = user_info)

if __name__ == '__main__':
    app.run(debug=True)
