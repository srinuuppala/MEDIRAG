const API_BASE = '/';

let currentReportId = null;

// Elements
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const analyzeBtn = document.getElementById('analyzeBtn');
const progressBar = document.getElementById('progressBar');
const progress = progressBar.querySelector('.progress');
const resultsSection = document.getElementById('results-section');
const reportIdSpan = document.getElementById('reportId');
const copyIdBtn = document.getElementById('copyId');
const errorDiv = document.getElementById('error');
const lookupIdInput = document.getElementById('lookupId');
const lookupBtn = document.getElementById('lookupBtn');
const lookupResults = document.getElementById('lookupResults');
const resultsGrid = document.getElementById('resultsGrid');

// Drag & Drop
uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('dragover');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('dragover');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('dragover');
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        fileInput.files = files;
        handleFileSelect();
    }
});

fileInput.addEventListener('change', handleFileSelect);

function handleFileSelect() {
    const file = fileInput.files[0];
    if (file) {
        analyzeBtn.disabled = false;
        analyzeBtn.innerHTML = `<i class="fas fa-magnifying-glass"></i> Analyze ${file.name}`;
    }
}

analyzeBtn.addEventListener('click', handleAnalyze);

async function handleAnalyze() {
    const file = fileInput.files[0];
    if (!file) return;

    showProgress(0);
    hideError();
    resultsSection.hidden = true;
    resultsGrid.innerHTML = '';
    lookupResults.innerHTML = '';

    const formData = new FormData();
    formData.append('file', file);

    try {
        showProgress(30);
        const response = await fetch(API_BASE + 'analyze', {
            method: 'POST',
            body: formData
        });

        showProgress(70);

        if (!response.ok) {
            const err = await response.text();
            throw new Error(err.includes('401') ? 'Invalid Groq API Key - check .env' : err);
        }

        const result = await response.json();
        renderSimpleResults(result);
        showProgress(100);
        setTimeout(() => progressBar.hidden = true, 1500);

        currentReportId = result.report_id;
    } catch (err) {
        console.error(err);
        showError(err.message);
        showProgress(0);
    }
}

function renderSimpleResults(data) {
    resultsSection.hidden = false;
    
    // Report ID
    reportIdSpan.textContent = data.report_id || 'N/A';
    
    // Medical Values
    const valuesCard = document.createElement('div');
    valuesCard.className = 'card values-card';
    valuesCard.innerHTML = `
        <h3><i class="fas fa-vials"></i> Medical Values</h3>
        <div id="medicalValues">
            ${Object.entries(data.medical_values || {}).map(([key, value]) => 
                `<div class="value-item"><strong>${key.replace(/_/g, ' ').toUpperCase()}:</strong> ${value}</div>`
            ).join('') || '<p>No values extracted</p>'}
        </div>
    `;
    resultsGrid.appendChild(valuesCard);
    
    // Analysis
    const analysisCard = document.createElement('div');
    analysisCard.className = 'card analysis-card';
    analysisCard.innerHTML = `
        <h3><i class="fas fa-chart-line"></i> Analysis</h3>
        <div id="analysis">${JSON.stringify(data.analysis || {}, null, 2)}</div>
    `;
    resultsGrid.appendChild(analysisCard);
    
    // Explanation - FULL TEXT
    const explanationCard = document.createElement('div');
    explanationCard.className = 'card full';
    explanationCard.style.gridColumn = '1 / -1';
    explanationCard.innerHTML = `
        <h3><i class="fas fa-file-alt"></i> 📝 Full Explanation</h3>
        <div id="explanation" class="full-explanation">${data.explanation || 'No explanation available'}</div>
    `;
    resultsGrid.appendChild(explanationCard);
    
    // Recommendations
    const recCard = document.createElement('div');
    recCard.className = 'card recommendations-card';
    recCard.innerHTML = `
        <h3><i class="fas fa-lightbulb"></i> Recommendations</h3>
        <div id="recommendations">${data.recommendations || 'Consult doctor'}</div>
    `;
    resultsGrid.appendChild(recCard);
}

copyIdBtn.addEventListener('click', () => {
    navigator.clipboard.writeText(currentReportId || '');
    const original = copyIdBtn.innerHTML;
    copyIdBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
    copyIdBtn.style.background = '#10b981';
    setTimeout(() => {
        copyIdBtn.innerHTML = original;
        copyIdBtn.style.background = '';
    }, 2000);
});

lookupBtn.addEventListener('click', handleLookup);

async function handleLookup() {
    const id = lookupIdInput.value.trim().toUpperCase();
    if (!id) return showError('Enter Report ID');

    try {
        const response = await fetch(API_BASE + `retrieve/${id}`);
        const data = await response.json();
        
        lookupResults.innerHTML = `
            <div class="card full">
                <h3>🔍 Retrieved Report: ${data.report_id}</h3>
                ${data.status === 'success' ? 
                    `<pre>${JSON.stringify(data.data, null, 2)}</pre>` :
                    `<p style="color: red;">${data.message}</p>`
                }
            </div>
        `;
    } catch (err) {
        showError('Retrieval failed');
    }
}

function showProgress(percent) {
    progress.style.width = Math.min(percent, 100) + '%';
    progressBar.hidden = percent === 0;
}

function showError(msg) {
    errorDiv.textContent = msg;
    errorDiv.style.display = 'block';
    setTimeout(hideError, 10000);
}

function hideError() {
    errorDiv.style.display = 'none';
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    document.body.style.opacity = '1';
});
