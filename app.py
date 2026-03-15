from flask import Flask, request, jsonify, send_from_directory
import os
import uuid
import tempfile
import shutil
from werkzeug.utils import secure_filename
from dotenv import load_dotenv




# Load environment variables
load_dotenv()

from workflows.medical_workflow import app as workflow_app
from utils.pdf_reader import load_pdf
from utils.ocr_reader import read_image
from rag.vector_store import store_report
from utils.report_id_generator import generate_report_id

app = Flask(__name__, static_folder='frontend', static_url_path='')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/analyze', methods=['POST'])
def analyze_report():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    filename = secure_filename(file.filename)
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, filename)
    file.save(file_path)
    
    try:
        file_lower = filename.lower()
        if file_lower.endswith('.pdf'):
            text = load_pdf(file_path)
        elif file_lower.endswith(('.png', '.jpg', '.jpeg', '.tiff')):
            text = read_image(file_path)
        else:
            return jsonify({'error': 'Unsupported file type. Use PDF or image.'}), 400
        
        if not text.strip():
            return jsonify({'error': 'No text extracted from file.'}), 400
        
        report_id = generate_report_id()
        
        state = {"text": text}
        result = workflow_app.invoke(state)
        
        full_content = f"Text: {text} | Analysis: {str(result)}"
        store_report(report_id, full_content)
        
        return jsonify({
            'report_id': report_id,
            'explanation': result.get("explanation", "No explanation generated."),
            'analysis': result.get("analysis", {}),
            'medical_values': result.get("medical_values", {}),
            'recommendations': "Consult a doctor for personalized advice."
        })
    
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

@app.route('/retrieve/<report_id>')
def retrieve_report(report_id):
    from rag.vector_store import get_report
    report = get_report(report_id)
    if report:
        return jsonify({
            "report_id": report_id,
            "status": "success",
            "data": report
        })
    return jsonify({
        "report_id": report_id,
        "status": "not_found",
        "message": "Report not found."
    })

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('frontend', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
