from flask import Flask, jsonify, request
app = Flask(__name__)

Jedi = [{'name' : 'Mace Windu'}, {'name' : 'Obi Wan Kenobi'}, {'name' : 'Ki Adi Mundi'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'Execute Order 66'})

#GET request
@app.route('/jedi' , methods=['GET'])
def showall():
    return jsonify({'Jedi' : Jedi})
@app.route('/jedi/<string:name>', methods=['GET'])
def show(name):
    jed = [jedi for jedi in Jedi if jedi['name'] == name]
    return jsonify({'jedi' : jed[0]})

@app.route('/jedi' , methods=['POST'])
def add():
    jedi = {'name' : request.json['name']}
    Jedi.append(jedi)
    return jsonify({'jedi' : jedi})

#PUT request
@app.route('/jedi/<string:name>', methods=['PUT'])
def edit(name):
    jed = [jedi for jedi in Jedi if jedi['name'] == name]
    jedi[0]['names'] = request.json['name']
    return jsonify({'jedi' : jed[0]})

#DELETE request
@app.route('/jedi/<string:name>', methods=['DELETE'])
def delete(name):
    jed = [jedi for jedi in Jedi if jedi['name'] == name]
    Jedi.remove(jed[0])
    return jsonify({'Jedi' : Jedi})
