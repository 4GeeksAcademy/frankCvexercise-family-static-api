"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")



    
# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_members():
    # this is how you can use the Family datastructure by calling its methods
    try:    
        members = jackson_family.get_all_members()
        response_body = {
            "family": members
        }
        if members == []:
            return jsonify({'error': 'Members not found'}),404
    
        return jsonify(response_body), 200
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message':str(e)}),500
    
@app.route('/members/<int:id>', methods=['GET'])
def handle_member(id):
    # this is how you can use the Family datastructure by calling its methods
    try:        
        if jackson_family.get_member(id)==None:
            # raise APIException("No such user!", status_code=404)
            return jsonify({"msg": 'not found member, id is wrong'}), 404
        
        member = jackson_family.get_member(id)
        return jsonify(member), 200
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message':str(e)}),500

@app.route('/members', methods=['POST'])
def handle_add_member():
    # this is how you can use the Family datastructure by calling its methods
    try:
        request_body = request.get_json(force='True')    
        if jackson_family.add_member(request_body) == None : 
            return jsonify({"msg": 'some field is missing, wrong body'}) ,404
        if jackson_family.add_member(request_body) == 'wrong age':
            return jsonify({"msg": 'wrong request body at age'}) ,404

        return jsonify(jackson_family.add_member(request_body)) ,201
    except Exception as e:
        return jsonify({'error':'Internal Server Error', 'message':str(e)}),500

@app.route('/members/<int:id>', methods=['DELETE'])
def handle_delete_member(id):
    # this is how you can use the Family datastructure by calling its methods
    try:
        if jackson_family.delete_member(id) == 'not found':
            return jsonify({"msg": 'wrong id'}) ,404
        else:
            jackson_family.delete_member(id)
            return jsonify(jackson_family.get_all_members()), 200
    except Exception as e:
         return jsonify({'error':'Internal Server Error', 'message':str(e)}),500


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
