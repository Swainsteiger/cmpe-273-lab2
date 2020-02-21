from flask import Flask, escape, request, jsonify
import json

app = Flask(__name__)
stud_id = 00000
class_id = 000000
DB = {
    "students":
        [
            {
                "first_name": "",
                "last_name": "",
                "id": 0
            }
        ],
    "classes":
        [
            {
                "class_name": "",
                "class_id": 0
            }
        ]
}


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/students', methods=['POST'])
def create_student():
    DB['students'].append({'id': request.form['stud_id'], 'first_name': request.form['first_name'],
                           'last_name': request.form['last_name']})
    print(DB)
    return "Student created."


@app.route('/students/<id>', methods=['GET'])
def get_student(id):
    for stud in DB['students']:
        if stud["id"] == request.view_args['id']:
            return jsonify({"student": stud})



@app.route('/classes', methods=['POST'])
def create_class():
    global DB
    DB['classes'].append({'class_id': request.form['class_id'], 'class_name': request.form['class_name']})
    print(DB)
    return "Class created."


@app.route('/classes/<class_id>', methods=['GET'])
def get_class(class_id):
    for cl in DB['classes']:
        if cl["class_id"] == request.view_args['class_id']:
            return jsonify({"Class": cl})


@app.route('/classes/<class_id>', methods=['PATCH'])
def update_class(class_id):
    stud = [stud for stud in DB['students'] if stud["id"] == request.form['stud_id']]
    index = 0
    for i in DB['classes']:
        index = index + 1
        if i["class_id"] == request.view_args['class_id']:
            break
    if 'students' in DB['classes'][index - 1]:
        DB['classes'][index - 1]['students'].append(stud)
    else:
        DB['classes'][index - 1].update({'students':stud})
    return jsonify({"Class": DB['classes'][index - 1]})
