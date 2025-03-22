from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Simple context processor to provide the current year for footer
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/results')
def results():
    """Render the results page with dummy data for UI preview"""
    # Dummy data for the UI
    zip_code = "12345"
    activities = ["Surfing", "Kiteboarding", "Fishing"]
    conditions = "Sunny with moderate wind"
    result = "This is a preview of the results page with dummy data."
    
    return render_template('results.html', 
                          zip_code=zip_code, 
                          activities=activities,
                          conditions=conditions,
                          result=result)

if __name__ == '__main__':
    app.run(debug=True)
