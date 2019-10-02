from flask import Flask, jsonify, request
from flasgger import Swagger
from flasgger import swag_from
import api_doc_specs.specs as const
import json
from shMongoDBLogic import ShMongoDBLogic as db

application = Flask(__name__)
application.config['SWAGGER'] = const.meta_swag
swagger = Swagger(application)

@application.route('/user/<user_email>/')
@swag_from(const.user_get, methods=['GET'], endpoint="get_user")
def getUser(user_email):
    """endpoint returning user information
    ---
 
    """
    result = db.getUserByEmail(user_email)
    if "_id" in result:
        del result["_id"] 
    pprint(result)
    return jsonify(result)

## This is really a POST, but Unity is whack-a-do with POST json
@application.route('/user', methods = ['POST'])
@swag_from(const.user_post)
def postUser():
    """
    endpoint for POSTting new user information.
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
        return jsonify({request.method : result})
    return jsonify({request.method : "failed"})


@application.route('/user', methods = ['PUT'])
@swag_from(const.user_post)
def putUser():
    """
    endpoint for PUTting new user information. Matches by email.
    ---
 
    """
    json = request.json
    user = db.getUserByEmail(json["Email"])
    result = "User does not exist"
    if "_id" in user: 
        for i in json:
            #print(user[i], end=" - ")
            user[i] = json[i]
            #print(user[i])
        result = db.editUser(user["Name"], user["Email"], user["Favorite_Color"], user["Superpower"], user["Field"], user["Favorite_Hobby"])
    return jsonify({request.method : result})

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