from flask import Flask, Blueprint
from flask_restplus import Resource, Api, Namespace, fields, reqparse

app = Flask(__name__)

api_v1 = Blueprint('api', __name__)

api = Api(app)
# api = Api(
#     api_v1, title='Covid-19 API :: v1', doc='/', version='1.0', 
#     # path='/api/v1/on-covid-19',
#     description='Covid-19 is a online tool to estimate the impact and severity of Covid-19.',)

# del api.namespaces[0]
# api.add_namespace(parcels_ns, path='/api/v1/auth')

@api.route('/api/v1/on-covid-19/json')
class InJson(Resource):
    def get(self):
        return {'hello': 'json'}
    def post(self):
        return {}

@api.route('/api/v1/on-covid-19/xml')
class InXml(Resource):
    def get(self):
        return {'hello': 'xml'}

@api.route('/api/v1/on-covid-19/logs')
class Logs(Resource):
    def get(self):
        return {'hello': 'logs'}

if __name__ == '__main__':
    app.run(debug=True)