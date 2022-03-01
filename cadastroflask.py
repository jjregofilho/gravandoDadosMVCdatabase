from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/signup', methods=['POST', 'GET'])
def post():  
    try:
        _name = request.form['name']
        _email = request.form['email']
        _password = request.form['password']

        if _name and _password and _email:
            conn = mysql.connect()
            cursor = conn.cursor()

            sql = "INSERT INTO tb_users(name, email, password) VALUES (%s, %s, %s)"
            value = (_name, _email, _password)

            cursor.execute(sql, value)
            conn.commit()

    except Exception as e:
        print("Problem inserting into db: " + str(e))
    finally:
        return render_template('index.html')


@app.route('/list', methods=['POST', 'GET'])
def index():
    conn = mysql.connect()
    cursor = conn.cursor()

    query = 'SELECT name, email, password FROM tb_users'
    cursor.execute(query)

    data = cursor.fetchall()

    return render_template('list.html', data=data)


if __name__ == '__main__':
    app.debug = True
    app.run()
    