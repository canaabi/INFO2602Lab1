from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/students')
def get_students():
    pref = request.args.get('pref')
    if pref:
        result = [
            student for student in data
            if 'pref' in student and student['pref'].lower() == pref.lower()
        ]
        return jsonify(result)
    return jsonify(data)


@app.route('/students/<id>')
def get_student(id):
    for student in data:
        if student.get('id') == id:
            return jsonify(student)
    return jsonify({'error': 'Student not found'}), 404


@app.route('/stats')
def get_stats():
    stats = {
        "Fish": 0,
        "Chicken": 0,
        "Vegetable": 0,
        "Computer Science (Major)": 0,
        "Computer Science (Special)": 0,
        "Information Technology (Major)": 0,
        "Information Technology (Special)": 0,
    }
    for student in data:
        pref = student.get('pref', '').title()
        if pref in stats:
            stats[pref] += 1
        programme = student.get('programme', '')
        if programme in stats:
            stats[programme] += 1
    return jsonify(stats)


@app.route('/add/<int:x>/<int:y>')
def addition(x, y):
    return jsonify(x + y)


@app.route('/sub/<int:x>/<int:y>')
def sub(x, y):
    return jsonify(x - y)


@app.route('/multiply/<int:x>/<int:y>')
def multiply(x, y):
    return jsonify(x * y)


@app.route('/divide/<int:x>/<int:y>')
def divide(x, y):
    return jsonify(x / y)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
