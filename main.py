from flask import Flask,render_template
import configs
from exts import db
from models import Book
from flask_restful import Api
from api import BookApi
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
# 加载配置文件
app.config.from_object(configs)
# db绑定app
db.init_app(app)
api= Api(app,default_mediatype='application/json')
api.add_resource(BookApi,'/book')
@app.route('/')
def index():
   data= Book.query.limit(10)
   return render_template('index.html',data=data)

@app.route('/detail/<id>')
def detail(id):
   data= Book.query.get(id)
   return render_template('detail.html',data=data)

if __name__ == '__main__':
   app.run()


