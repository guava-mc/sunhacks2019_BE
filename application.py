from flask import Flask, jsonify, request
from flasgger import Swagger
from flasgger import swag_from
import api_doc_specs.specs as const
import json
from shMongoDBLogic import ShMongoDBLogic as db

application = Flask(__name__)
application.config['SWAGGER'] = const.meta_swag
swagger = Swagger(application)

@application.route('/getUser/<user_email>/')
@swag_from(const.user_get, methods=['GET'])
def getUser(user_email):
    """endpoint returning user information
    ---
 
    """
    result = db.getUserByEmail(user_email)
    del result["_id"] 
    pprint(result)
    return jsonify(result)

@application.route('/addUser', methods = ['PUT'])
@swag_from(const.user_put)
def productsPost():
    """
    endpoint for PUTting new user information.
    ---
 
    """
    print(request)
    json = request.json
    pprint(json)
    if len(json) > 0:
        # {"Name":"Stephanie Miranda","Email":"smirand6@asu.edu",
        #"Favorite_Color":"425caa","Superpower":"levitation",
        #"Field":"software engineering","Favorite_Hobby":"doodling"}
        result = db.addUser(json["Name"], json["Email"], json["Favorite_Color"], json["Superpower"], json["Field"], json["Favorite_Hobby"])
        return jsonify({"PUT" : result})
    return jsonify({"PUT" : "failed"})

@application.route('/getSponsor/<sponsor_name>/')
@swag_from(const.sponsor_get, methods=['GET'])
def getSponsor(sponsor_name):
    """endpoint returning sponsor information
    ---
 
    """
    print(sponsor_name)
    result = db.getCompanyByName(sponsor_name)
    del result["_id"] 
    pprint(result)
    return jsonify(result)

def pprint(py_dict):
	print(json.dumps(py_dict, sort_keys=True,indent=4, separators=(',', ': ')))

if(__name__=="__main__"):
    application.run(debug=True)