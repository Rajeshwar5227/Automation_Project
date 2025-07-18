from flask import Flask, render_template_string, request, redirect, url_for, send_from_directory, jsonify
import subprocess
import os
import re
from datetime import datetime
import threading
import time

app = Flask(__name__)

# Paths
TESTS_DIR = 'tests'
REPORT_PATH = 'reports/report.html'
PYTEST_INI = 'pytest.ini'

# Shared state for progress
progress_data = {
    'total': 0,
    'completed': 0,
    'running': False,
    'exec_time': None,
    'total_time': None,
    'report_url': None,
    'selected_script': None,
    'selected_marker': None,
    'tests': []  # NEW: List of dicts, one per test
}
progress_lock = threading.Lock()

# Read available test scripts
def get_test_scripts():
    return [f for f in os.listdir(TESTS_DIR) if f.startswith('test_') and f.endswith('.py')]

# Read available markers from pytest.ini
def get_markers():
    markers = []
    if os.path.exists(PYTEST_INI):
        with open(PYTEST_INI, 'r') as f:
            content = f.read()
            match = re.search(r'markers\s*=([\s\S]+)', content)
            if match:
                marker_lines = match.group(1).strip().split('\n')
                for line in marker_lines:
                    marker = line.split(':')[0].strip()
                    if marker:
                        markers.append(marker)
    return markers

def count_test_cases(script_path, marker=None):
    # Count test functions in the script, optionally filtered by marker
    count = 0
    with open(script_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    marker_active = marker is None
    for i, line in enumerate(lines):
        if marker:
            if f'@pytest.mark.{marker}' in line:
                marker_active = True
            elif line.strip().startswith('def test_'):
                if marker_active:
                    count += 1
                marker_active = False
        else:
            if line.strip().startswith('def test_'):
                count += 1
    return count

def count_test_cases_and_names(script_path, marker=None):
    # Returns (count, [test_names])
    count = 0
    test_names = []
    with open(script_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    marker_active = marker is None
    for i, line in enumerate(lines):
        if marker:
            if f'@pytest.mark.{marker}' in line:
                marker_active = True
            elif line.strip().startswith('def test_'):
                if marker_active:
                    test_name = line.strip().split()[1].split('(')[0]
                    test_names.append(test_name)
                    count += 1
                marker_active = False
        else:
            if line.strip().startswith('def test_'):
                test_name = line.strip().split()[1].split('(')[0]
                test_names.append(test_name)
                count += 1
    return count, test_names

def run_pytest_in_background(script, marker):
    script_path = os.path.join(TESTS_DIR, script)
    total_tests, test_names = count_test_cases_and_names(script_path, marker)
    with progress_lock:
        progress_data['total'] = total_tests
        progress_data['completed'] = 0
        progress_data['running'] = True
        progress_data['exec_time'] = None
        progress_data['total_time'] = None
        progress_data['report_url'] = None
        progress_data['selected_script'] = script
        progress_data['selected_marker'] = marker
        progress_data['tests'] = [{'name': name, 'status': 'PENDING'} for name in test_names]
    cmd = [
        'pytest',
        script_path,
        '-m', marker,
        '--html', REPORT_PATH,
        '--self-contained-html',
        '-v'
    ]
    start_time = datetime.now()
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    completed = 0
    for line in process.stdout:
        # Look for lines like: test_foo.py::test_bar PASSED
        match = re.match(r'.*::(test_[\w_]+)\s+(PASSED|FAILED|SKIPPED|ERROR)', line)
        if match:
            test_name = match.group(1)
            status = match.group(2)
            completed += 1
            with progress_lock:
                progress_data['completed'] = completed
                # Update the status for this test
                for test in progress_data['tests']:
                    if test['name'] == test_name:
                        test['status'] = status
                        break
    process.wait()
    end_time = datetime.now()
    with progress_lock:
        progress_data['exec_time'] = end_time.strftime('%Y-%m-%d %H:%M:%S')
        progress_data['total_time'] = str(end_time - start_time)
        progress_data['report_url'] = '/' + REPORT_PATH.replace('\\', '/')
        progress_data['running'] = False

# HTML template with progress bar and JS polling
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dashboard</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body class="bg-light">
<div class="container py-5">
    <h2 class="mb-4">Dashboard</h2>
    <form id="runForm" method="post" action="/run">
        <div class="row g-3 align-items-end">
            <div class="col-md-4">
                <label for="script" class="form-label">Select Test Script</label>
                <select class="form-select" id="script" name="script" required {% if running %}disabled{% endif %}>
                    <option value="" disabled selected>Select a script...</option>
                    {% for script in scripts %}
                    <option value="{{ script }}" {% if script == selected_script %}selected{% endif %}>{{ script }}</option>
                    {% endfor %}
                </select>
            </div>
            <div class="col-md-4">
                <label for="marker" class="form-label">Select Marker</label>
                <select class="form-select" id="marker" name="marker" required {% if running %}disabled{% endif %}>
                    <option value="" disabled selected>Select a marker...</option>
                    {% for marker in markers %}
                    <option value="{{ marker }}" {% if marker == selected_marker %}selected{% endif %}>{{ marker }}</option>
                    {% endfor %}
                </select>
            </div>
            <div class="col-md-2 d-flex">
                <button type="submit" class="btn btn-primary me-2 w-100" {% if running %}disabled{% endif %}>Run</button>
                <a href="/reset" class="btn btn-secondary w-100">Reset</a>
            </div>
        </div>
    </form>
    <div id="progressSection" class="mt-4" style="display:none;">
        <label class="form-label">Progress:</label>
        <div class="progress">
            <div id="progressBar" class="progress-bar progress-bar-striped progress-bar-animated bg-success" role="progressbar" style="width: 0%">0%</div>
        </div>
        <div id="progressText" class="mt-2"></div>
    </div>
    <div id="testStatusSection" class="mt-3" style="display:none;">
        <label class="form-label">Test Details:</label>
        <table class="table table-sm table-bordered">
            <thead>
                <tr>
                    <th>Test Name</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody id="testStatusTable">
            </tbody>
        </table>
    </div>
    <div id="resultSection" class="mt-4" style="display:none;">
        <table class="table table-bordered table-striped align-middle bg-success bg-opacity-10 border-success">
            <thead class="table-success">
                <tr>
                    <th scope="col">Result</th>
                    <th scope="col">Execution Time</th>
                    <th scope="col">Total Time Taken</th>
                    <th scope="col">HTML Report</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Test run complete!</strong></td>
                    <td id="execTime"></td>
                    <td id="totalTime"></td>
                    <td><a id="reportLink" href="#" target="_blank" class="btn btn-success btn-sm">View HTML Report</a></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
<script>
$(function() {
    var running = {{ 'true' if running else 'false' }};
    function pollProgress() {
        $.getJSON('/progress', function(data) {
            // Update per-test status table
            var rows = '';
            if (data.tests) {
                data.tests.forEach(function(test) {
                    var status = test.status;
                    var color = status === 'PASSED' ? 'text-success' :
                                status === 'FAILED' ? 'text-danger' :
                                status === 'SKIPPED' ? 'text-warning' :
                                status === 'ERROR' ? 'text-danger' : 'text-secondary';
                    rows += '<tr><td>' + test.name + '</td><td class="' + color + '">' + status + '</td></tr>';
                });
            }
            $('#testStatusTable').html(rows);

            // Always show the test status section if there are tests
            if (data.tests && data.tests.length > 0) {
                $('#testStatusSection').show();
            } else {
                $('#testStatusSection').hide();
            }

            if (data.running) {
                $('#progressSection').show();
                var percent = data.total > 0 ? Math.round(100 * data.completed / data.total) : 0;
                $('#progressBar').css('width', percent + '%').text(percent + '%');
                $('#progressText').text('Completed ' + data.completed + ' of ' + data.total + ' tests...');
                $('#resultSection').hide();
                setTimeout(pollProgress, 1000);
            } else if (data.total > 0) {
                $('#progressSection').hide();
                $('#resultSection').show();
                $('#execTime').text(data.exec_time);
                $('#totalTime').text(data.total_time);
                $('#reportLink').attr('href', data.report_url);
            }
        });
    }
    $('#runForm').on('submit', function(e) {
        $('#progressSection').show();
        $('#progressBar').css('width', '0%').text('0%');
        $('#progressText').text('Starting...');
        $('#resultSection').hide();
        setTimeout(pollProgress, 1000);
    });
    if (running) {
        $('#progressSection').show();
        pollProgress();
    }
});
</script>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    scripts = get_test_scripts()
    markers = get_markers()
    with progress_lock:
        running = progress_data['running']
        selected_script = progress_data['selected_script']
        selected_marker = progress_data['selected_marker']
    return render_template_string(
        HTML_TEMPLATE,
        scripts=scripts,
        markers=markers,
        running=running,
        selected_script=selected_script,
        selected_marker=selected_marker
    )

@app.route('/run', methods=['POST'])
def run_tests():
    script = request.form['script']
    marker = request.form['marker']
    # Start pytest in background thread
    t = threading.Thread(target=run_pytest_in_background, args=(script, marker), daemon=True)
    t.start()
    with progress_lock:
        progress_data['running'] = True
        progress_data['selected_script'] = script
        progress_data['selected_marker'] = marker
    return redirect(url_for('index'))

@app.route('/progress')
def progress():
    with progress_lock:
        return jsonify(progress_data)

@app.route('/reset')
def reset():
    with progress_lock:
        progress_data['selected_script'] = None
        progress_data['selected_marker'] = None
        progress_data['total'] = 0
        progress_data['completed'] = 0
        progress_data['running'] = False
        progress_data['exec_time'] = None
        progress_data['total_time'] = None
        progress_data['report_url'] = None
        progress_data['tests'] = []
    return redirect(url_for('index'))

# Serve the HTML report statically
@app.route('/reports/<path:filename>')
def serve_report(filename):
    return send_from_directory('reports', filename)

if __name__ == '__main__':
    app.run(debug=True) 