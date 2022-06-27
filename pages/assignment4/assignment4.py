import json

import requests
from flask import Blueprint, render_template, redirect, flash
from flask import url_for
from datetime import timedelta
from flask import request, session, jsonify
import mysql.connector

assignment4 = Blueprint(
    'assignment4'
    , __name__,
    static_folder='static',
    static_url_path='/pages/assignment4',
    template_folder='templates'
)


@assignment4.route('/assignment4')
def index():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment4.html', users=users_list)


@assignment4.route('/assignment4/users')
def users_json():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return jsonify(users_list)


@assignment4.route('/assignment4/outer_source')
def fetch_json():
    return render_template('outer_source.html')


@assignment4.route('/fetch_be')
def fetch_be_func():
    if 'num' in request.args:
        number = request.args['num']
        res = requests.get(f'https://reqres.in/api/users/{number}')
        res = res.json()
        print(res)
        if (res == {}):
            return render_template('outer_source.html', massage="There is no such user")
        print(res)
        res = res['data']
        return render_template('outer_source.html', fname=res['first_name'], lname=res['last_name'], email=res['email'],
                               avatar=res['avatar'])

@assignment4.route('/assignment4/restapi_users')
def restapi():
    query = "select * from users limit 1"
    users_list = interact_db(query, query_type='fetch')
    return jsonify(users_list)


@assignment4.route('/assignment4/restapi_users/<id>')
def restapi_id(id):
    # if id is None:
    #     print("dsfsdfsdf")
    #     query = "select * from users limit 1"
    #     users_list = interact_db(query, query_type='fetch')
    #     return jsonify(users_list)
    query = "select * from users where id='%s';" % (id)
    users_list = interact_db(query, query_type='fetch')
    if (users_list == []):
        return jsonify("There is no such user")
    return jsonify(users_list)


@assignment4.route('/insert_user', methods=['POST'])
def insert_user():
    name = request.form['name']
    email = request.form['email']
    if check_exist(name):
        flash("user already exist")
        return redirect('/assignment4')
    query = "INSERT INTO users(u_name, email) VALUES ('%s', '%s')" % (name, email)
    interact_db(query=query, query_type='commit')
    flash("user inserted successfully")
    return redirect('/assignment4')


@assignment4.route('/update_user', methods=['POST'])
def update_user_func():
    user_name = request.form['user_name']
    user_email = request.form['user_email']
    if not check_exist(user_name):
        flash("There is no such user")
        return redirect('/assignment4')
    query = "UPDATE users SET email='%s' WHERE u_name='%s';" % (user_email, user_name)
    interact_db(query, query_type='commit')
    flash("user updated successfully")
    return redirect('/assignment4')


@assignment4.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['user_id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query, query_type='commit')
    flash("user deleted successfully")
    return redirect('/assignment4')


def check_exist(name):
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    for user in users_list:
        if name == user.u_name:
            return True
    return False


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='Root',
                                         database='myflaskappdb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value
