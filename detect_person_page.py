from flask import Blueprint, jsonify, request

detect_person_api = Blueprint('detect_person_api', __name__, template_folder='templates')

# sample : {base_url}/detect
@detect_person_api.route('/detect', methods=['GET'])
def meat_consumption_pie():
    args = request.args

    is_person_present = True
    person_count = 3

    result = {'is_person_present': int(is_person_present), 'person_count': str(person_count)}

    return jsonify(result)
