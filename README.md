Waterman.AI
A sleek, minimalist Flask web app for ocean activity forecasts.
Overview
Waterman.AI provides personalized forecasts for water activities based on location and preferred conditions. This repo contains a clean frontend implementation ready for backend integration.
Features

Simple, modern dark-mode UI
Location-based forecast requests
Customizable ideal conditions input
Responsive design for all devices

Installation

Clone the repository

bashCopygit clone https://github.com/yourusername/waterman-ai.git
cd waterman-ai

Install dependencies

bashCopypip install flask

Run the application

bashCopypython app.py

Access at http://127.0.0.1:5000

Project Structure
Copywaterman-ai/
├── app.py                  # Flask application
├── templates/              # HTML templates
│   ├── base.html           # Base template with layout
│   ├── index.html          # Main form page
│   └── results.html        # Results display page
└── static/                 # Static assets
    ├── css/                # Stylesheets
    │   └── style.css       # Main CSS
    └── js/                 # JavaScript
        └── main.js         # Main JS functionality
Contributing
Contributions are welcome! Feel free to submit a Pull Request.
License
MIT

Created by Mike Kozub
