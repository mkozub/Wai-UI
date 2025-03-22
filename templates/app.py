from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Add current_year function to template context
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/results')
def results():
    """Process the form and display results"""
    # Get parameters from the request URL (from form submission)
    zip_code = request.args.get('location', '12345')
    conditions = request.args.get('free_text', 'Not specified')
    
    # Generate a sample result message
    result = f"Weather analysis for {zip_code}: The current conditions are favorable for your activities based on your preferences for {conditions}."
    
    # Render the results template with the form data
    return render_template('results.html', 
                          zip_code=zip_code, 
                          conditions=conditions,
                          result=result)

if __name__ == '__main__':
    app.run(debug=True)
