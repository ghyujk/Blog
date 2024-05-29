import sqlite3 #引入sqlite3
from flask import Flask , render_template

app = Flask(__name__) # 创建一个Flask对象

# 创建一个函数用来获取数据库链接
def get_db_connection():
    # 创建数据库链接到database.db文件
    conn = sqlite3.connect('database.db')
    # 设置数据的解析方法，有了这个设置，就可以像字典一样访问每一列数据
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/') # 装饰器
def index():
    conn = get_db_connection()
    posts = conn.execute('selest * from posts').fetchall()
    # 指定当前网页要使用index.html网页
    return render_template('index.html' , posts = posts)





