from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Greeting (Resource):
    def get(self):
<<<<<<< HEAD
        return 'Hello People'
=======
        return 'Hello  Sunday Good !!!!'
>>>>>>> 920300d9c3265c7065be0ccd22468b60bcc43c32

api.add_resource(Greeting, '/') # Route_1

if __name__ == '__main__':
    app.run('0.0.0.0','3333')
