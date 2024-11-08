from flask import jsonify
from flask_restful import Resource,fields,marshal_with,reqparse,inputs

from .models import User,User2

class HomeResource(Resource):

    def get(self):
        user = User2.query.first()

        return jsonify({
            'id' : user.id,
            'name' : user.name,
            'like' : user.like,
            'hobby' : user.hobby,
            'test' : user.test
        })

    def post(self):

        pass


ret_field = {
    'status':fields.Integer,
    'msg':fields.String,
    'data2':fields.String(attribute='data'),     # 关联函数返回值中data的值
    'like':fields.String(default='read'),
    'url':fields.Url(endpoint=id,absolute=True)     # 跳转链接、绝对路径
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
parser.add_argument('url',type=inputs.url,required=True,help='name is required!')


class PersonResource(Resource):
    def get():
        args = parser.parse_args()
        name = args.get('name')

        return {
            'name':name
        }