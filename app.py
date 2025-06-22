from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html') as f:
        return render_template_string(f.read())

@app.route('/process', methods=['POST'])
def process():
    data = request.json.get('csv', '')
    lines = data.strip().split('\n')
    result = []
    for line in lines:
        parts = line.split(',')
        if len(parts) > 2:
            result.append(parts[0] + ',' + ','.join(parts[2:]))
        else:
            result.append(line)
    return jsonify({'output': '\n'.join(result)})

if __name__ == '__main__':
    app.run(debug=True)
