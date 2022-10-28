from flask import Flask, render_template
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host='34.142.180.39',
    port = 13306,
    user='root',
    password='oh_my_ody!',
    db='data_center',
    charset='utf8'
)

@app.route('/')
def hello_world():
    cur = conn.cursor()

    sql = "select channel_id from channel GROUP BY channel_id"
    cur.execute(sql)
    content = cur.fetchall()

    sql = "SHOW FIELDS FROM channel"
    cur.execute(sql)
    #labels = cur.fetchall()
    #labels = [l[0] for l in labels]

    #return render_template('index.html', labels=labels, content=content)
    return render_template('index.html',  content=content)

if __name__ == '__main__':
    app.run()


"# SQL" 
