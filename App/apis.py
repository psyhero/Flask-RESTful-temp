from flask import jsonify
from flask_restful import Resource,fields,marshal_with,reqparse
from .models import User
from .extentions import cache


class HelloResource(Resource):

    @cache.cached(timeout=60)
    def get(self):

        pass

    def post(self):

        pass


ret_field = {
    'status':fields.Integer,
    'msg':fields.String,
    'data2':fields.String(attribute='data'),     # 关联data的值
    'like':fields.String(default='read'),
    'url':fields.Url(endpoint=id,absolute=True)
}

class UserResource(Resource):
    
    @marshal_with(ret_field)
    def get():
        user = User.query.first()

        return jsonify({
            'status':1,
            'msg':'OK',
            'data':user,
            # 'like':'Sing'
        })
    



parser = reqparse.RequestParser()
parser.add_argument('name',type=str,required=True,help='name is required!')


class PersonResource(Resource):
    def get():
        args = parser.parse_args()
        name = args.get('name')

        return {
            'name':name
        }