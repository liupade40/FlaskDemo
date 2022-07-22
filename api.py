from flask_restful import Resource
from models import Book
class BookApi(Resource):
    def get(self):
        data= Book.query.limit(10)
        list=[]
        for d in data:
            list.append({'id':d.id,'name':d.name,'author':d.author})
        return list
