from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysql'        # Use 'mysql' in Docker, 'localhost' locally
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL(app)

@app.before_request
def create_tables():
    cur = mysql.connection.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(80) NOT NULL
        )
    """)
    mysql.connection.commit()
    cur.close()

@app.route('/')
def index():
    # Example: Display form and list of users
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s)", [name])
    mysql.connection.commit()
    cur.close()
    return 'User added'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

