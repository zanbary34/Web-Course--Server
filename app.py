from datetime import timedelta

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)


app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)

@app.route('/')
@app.route('/home')
def index_func():
    return render_template('Home.html')


@app.route('/contact')
def about_page():
    user_info = {'name': "Jack", "second_name": "Sparo"}
    degrees = []
    hobbies = ()
    return render_template('Contact.html', user_info=user_info)


@app.route('/assignment3_1')
def movies_page():
    favor_movies = {"movie": ["The Shawshank Redemption", "The Dark Knight", "Pulp Fiction", "The Godfather"],
                    "star": ["Tim Robbins", "Christian Bale", "John Travolta", "Marlon Brando"],
                    "year": [1994, 2008, 1994, 1972]}
    return render_template('assignment3_1.html', favor_movies=favor_movies)


users = {1: {"name": "Yossi", "email":
    "yo@gmail.com"}, 2: {"name": "Arie", "email":
    "ar@gmail.com"}, 3: {"name": "Moshe", "email":
    "mo@gmail.com"}, 4: {"name": "Haim", "email":
    "ha@gmail.com"}, 5: {"name": "Yoram", "email":
    "yor@gmail.com"}}


@app.route('/assignment3_2', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        username = request.form['uname_r']
        email = request.form['email_r']
        for user in users:
            if username == users[user]["name"]:
                return render_template('assignment3_2.html', massage_wrong="User name already exist")

        users.update({list(users.keys())[-1]+1: {"name": username, "email": email}})
        session['username'] = username
        session['logedin'] = True
        return redirect('/home')
    elif 'uname' in request.args:
        u_name = request.args['uname']
        for user in users:
            if users[user]["name"] == u_name:
                email_address = users[user]["email"]
                return render_template('assignment3_2.html', u_name=u_name, email_address=email_address)
            if u_name == "":
                return render_template('assignment3_2.html', users=users)
    return render_template('assignment3_2.html')

@app.route('/log_out')
def log_out():
    session['logedin'] = False
    session.clear()
    return redirect(url_for('log_in'))

# if request.method == "POST":


# elif request.method =='Post':
#     user_name = request.args['uname']
#     email_address = request.args['email']
#     users.update({count: {"name": user_name,"email":email_address}})

if __name__ == '__main__':
    app.run(debug=True)
