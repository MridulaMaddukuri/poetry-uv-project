from boilerplate_poetry_project import add, multiply
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/add", methods=["POST"])
def add_numbers():
    # Get data from the request
    try:
        data = request.get_json()
        x = data["x"]
        y = data["y"]
    except (KeyError, TypeError):
        return jsonify(
            {
                "error": 'Invalid request format. Please provide JSON with keys "x" and "y" (integers)'
            }
        ), 400

    # Call the add function from the imported script
    try:
        result = add.add_int(x, y)
    except TypeError as e:
        return jsonify({"error": str(e)}), 400

    # Return the result as JSON
    return jsonify({"result": result})


@app.route("/multiply", methods=["POST"])
def multiply_numbers():
    # Get data from the request
    try:
        data = request.get_json()
        x = data["x"]
        y = data["y"]
    except (KeyError, TypeError):
        return jsonify(
            {
                "error": 'Invalid request format. Please provide JSON with keys "x" and "y" (integers)'
            }
        ), 400

    # Call the multiply function from the imported script
    try:
        result = multiply.multiply_int(x, y)
    except TypeError as e:
        return jsonify({"error": str(e)}), 400

    # Return the result as JSON
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
