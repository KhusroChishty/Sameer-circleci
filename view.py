from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message": "Hello, World!"})
fetch('/config.json')
  .then(response => response.json())
  .then(config => {
    const apiUrl = config.apiEndpoint;
