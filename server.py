from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域请求

@app.route('/run-program', methods=['POST'])
def run_program():
    data = request.json
    command = data.get('command')
    try:
        # Use subprocess to run the command
        subprocess.Popen(command, shell=True)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='127.0.0.1', port=5000)
