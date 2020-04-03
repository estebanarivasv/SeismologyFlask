from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api

import main.resources as resources

api = Api()


def create_app():

    app = Flask(__name__)

    load_dotenv()

    api.add_resource(resources.SensorResource, '/sensor/<id_num>')
    api.add_resource(resources.SensorsResource, '/sensors')
    api.add_resource(resources.UnverifiedSeismResource, '/unverified-seism/<id_num>')
    api.add_resource(resources.UnverifiedSeismsResource, '/unverified-seisms')
    api.add_resource(resources.VerifiedSeismResource, '/verified-seism/<id_num>')
    api.add_resource(resources.VerifiedSeismsResource, '/verified-seisms')

    api.init_app(app)

    return app

