from flask import Flask
from flask_restful import Api
from ncdcapi import ncdc

app = Flask(__name__)
api = Api(app)

api.add_resource(ncdc,"/")

if __name__ == "__main__":
  app.run()