from flask import Flask, escape, request, jsonify
import json

app = Flask(__name__)

DB = {
    "students": [],
    "classes": []
}


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/students', methods=['POST'])
def create_student():
    global id, data
    DB['students'].append({'id' : id, 'first_name': request.form['name']})
    student = [stud for stud in DB['students'] if stud["first_name"] == (request.form['name'])]
    id = id+1
    return jsonify({"student":student})


@app.route('/students/<id>', methods=['GET'])
def get_student(id):
    student = [stud for stud in DB['students'] if stud["id"] == int(request.view_args['id'])]
    return jsonify({"student": student})


@app.route('/classes', methods=['POST'])
def create_class():
    global class_id, data
    DB['classes'].append({'class_id': class_id, 'class_name': request.form['name']})
    student = [stud for stud in data['classes'] if stud["class_name"] == (request.form['name'])]
    class_id = class_id + 1
    return jsonify({"Class": student})


@app.route('/classes', methods=['GET'])
def get_class():
    cl = [cl for cl in DB['classes'] if cl["class_id"] == int(request.view_args['id'])]
    return jsonify({"Class": cl})


@app.route('/classes/<id>', methods=['PATCH'])
def update_class(id):
    stud = [stud for stud in DB['students'] if stud["id"] == int(request.form['student_id'])]
    index = 0
    for x in DB['classes']:
        index = index + 1
        if x["class_id"] == int(request.view_args['id']):
            cl = x
            break

    if 'students' in cl:
        flag = False
        for y in cl['students']:
            if y['id'] == int(request.form['student_id']):
                flag = True
                return "Student already registered in this class"
        if not flag:
            DB['classes'][index - 1]['students'].extend(stud)
    else:
        DB['classes'][index - 1].update({'students': stud})

    return jsonify({"Class": cl})
