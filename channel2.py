from flask import Flask
import pymysql
import string

app = Flask(__name__)

conn = pymysql.connect(
    host = '34.142.180.39',
    port = 13306,
    user = 'root',
    password = 'oh_my_ody!',
    db = 'data_center',
    charset = 'utf8'
)

cur = conn.cursor()
cur.execute("SELECT  COUNT(uuid)  FROM channel")
r = cur.fetchall()
stri = ''.join(str(r))
punctuation_string = string.punctuation

for i in punctuation_string:
    stri = stri.replace(i,'')
print(stri)

@app.route("/")

def test_channel(): 
    return (stri)

if __name__ == "__main__":
    app.run()

