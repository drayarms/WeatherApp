from flask import Flask, jsonify, request, send_from_directory

from flask_cors import CORS

app = Flask(__name__, static_folder='../my-react-app/build')

CORS(app)  # Allow CORS for all routes and origins

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello from Flask :)"}
    return jsonify(data)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
