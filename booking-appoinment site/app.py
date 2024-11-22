from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# 创建数据库和表
def init_db():
    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            date TEXT,
            time TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    email = request.form['email']
    date = request.form['date']
    time = request.form['time']
    message = request.form['message']

    # 存储数据到数据库
    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO appointments (name, email, date, time, message) VALUES (?, ?, ?, ?, ?)',
                   (name, email, date, time, message))
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": "Appointment booked successfully!"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
