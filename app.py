from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Ensure index.html is in 'templates' folder

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    if not data or 'csv' not in data:
        return jsonify({'error': 'No CSV data provided'}), 400

    lines = data['csv'].strip().split('\n')
    processed = []
    for line in lines:
        parts = line.split(',')
        if len(parts) > 2:
            processed.append(parts[0] + ',' + ','.join(parts[2:]))
        else:
            processed.append(line)

    return jsonify({'output': '\n'.join(processed)})

if __name__ == '__main__':
    app.run(debug=True)

