import json

from exts import db

"""
 Integer	整型
String	字符串
Text	文本
DateTime	日期
Float	浮点型
Boolean	布尔值
PickleType	存储一个序列化（ Pickle ）后的Python对象
LargeBinary	巨长度二进制数据 
"""

def to_json(inst,cls):
    d=dict()
    for c in cls.__table__.columns:
        v=getattr(inst,c.name)
        d[c.name]=v
    return  json.dump(d)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float(255))
    author = db.Column(db.String(255))
    img_url = db.Column(db.String(50))
    desc = db.Column(db.String(5000))
    createtime = db.Column(db.DateTime())

    @property
    def serialize(self):
        return  to_json(self,self.__class__)

class BookUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    url = db.Column(db.String(255))
    createtime = db.Column(db.DateTime())