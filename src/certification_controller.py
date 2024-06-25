import json
from flask import Flask, request, Blueprint, jsonify

certification_controller_bp = Blueprint('certification_controller', __name__)


@certification_controller_bp.route('/uploadPdf', methods=['POST'])
def uploadPdf():
    intput_question = json.loads(request.data)
    print("Question: ", intput_question);
    return ""