import uuid

def generate_report_id():
    """Generate unique 8-char report ID."""
    return str(uuid.uuid4()).replace('-', '').upper()[:8]

