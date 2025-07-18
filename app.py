from flask import Flask, render_template_string, jsonify
import subprocess

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Run Dashboard Tests</title>
</head>
<body>
    <h1>Run Dashboard Tests</h1>
    <button id="startBtn">Start</button>
    <pre id="output"></pre>
    <script>
        document.getElementById('startBtn').onclick = function() {
            fetch('/run', {method: 'POST'})
                .then(response => response.json())
                .then(data => {
                    document.getElementById('output').textContent = data.output;
                });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/run', methods=['POST'])
def run_script():
    try:
        result = subprocess.run(
            ['python', 'run_tests_dashboard.py'],
            capture_output=True, text=True, check=True
        )
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = e.output or str(e)
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True) 