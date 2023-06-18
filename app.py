from flask import Flask, request, jsonify, json
from annotation_converter.converter import convert

app = Flask(__name__)
json.provider.DefaultJSONProvider.sort_keys = False

@app.route('/convert', methods=['GET'])
def process_route():
    # Get the filename
    file_name = request.args.get('filename')

    # Call converter with the file
    result = convert(file_name)

    # Return the result as a response
    return jsonify(result)

if __name__ == '__main__':
    app.run()
