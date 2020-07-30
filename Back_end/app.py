from flask import Flask, request
from flask_cors import CORS, cross_origin
import random
import json
app = Flask('RPN')


# set the cors policy to allow requests from any client
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# List of all the stacks
stacks = {"453135": [2, 6],
          "789456": [1,6,8]}


def generate_id():
    """Generate an id for a new stack"""
    new_id = random.randint(0, 100000)
    while new_id in stacks:
        new_id = random.randint(0, 100000)
    return str(new_id)


@app.route('/')
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def home():
    return 'RPN API'


@app.route('/rpn/op', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type', 'Authorization'])
def get_list_of_operands():
    """Get the list of all operands"""
    return {"operations": ["+", "-", "/", "*"]}


@app.route('/rpn/stack', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Content-Type', 'Authorization'])
def list_of_stack():
    if request.method == 'GET':
        """Get all the stacks"""
        ids = []
        for key, value in stacks.items():
            ids.append(key)
        return {"stacks": ids}
    if request.method == 'POST':
        """Create a new stack"""
        stacks[generate_id()] = []
        return {"status": "ok"}


@app.route('/rpn/op/<string:op>/stack/<stackid>', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def apply_operation(op, stackid):
    print(request.data)
    stack = stacks[stackid]
    element = stack.pop(-1)
    el = stack.pop(-1)
    if op == '/':
        stack.append(el / element)
    elif op == '*':
        stack.append(el * element)
    elif op == '+':
        stack.append(el + element)
    elif op == '-':
        stack.append(el - element)
    stacks[stackid] = stack
    print(stacks)
    return{"status": "ok"}


@app.route('/rpn/stack/<stackid>', methods=['GET', 'POST', 'DELETE'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def stack(stackid):
    if stackid == 'undefined':
        print("stackid is missing")
        return {"status": "stackid is missing"}
    if request.method == 'GET':
        """Get a stack"""
        return {"stack": stacks[stackid]}
    if request.method == 'POST':
        """Add a value in a stack"""
        data = json.loads(request.data.decode("utf-8"))
        if "value" in data:
            value = data["value"]
            print(value)
            stacks[stackid].append(int(value))
            return {"status": "ok"}
        print("value is missing")
        return {"status": "value is missing"}
    if request.method == 'DELETE':
        """Delete a stack"""
        stacks.pop(stackid)
        return {"status": "ok"}


if __name__ == '__main__':
    app.config['Access-Control-Allow-Origin'] = '*'
    app.run()
