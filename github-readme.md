# Waterman.AI

A sleek, minimalist Flask web app for ocean activity forecasts.

## Overview

Waterman.AI provides personalized forecasts for water activities based on location and preferred conditions. This repo contains a clean frontend implementation ready for backend integration.

## Features

- Simple, modern dark-mode UI
- Location-based forecast requests
- Customizable ideal conditions input
- Responsive design for all devices

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/waterman-ai.git
cd waterman-ai
```

2. Install dependencies
```bash
pip install flask
```

3. Run the application
```bash
python app.py
```

4. Access at `http://127.0.0.1:5000`

## Project Structure

```
waterman-ai/
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
```

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.

## License

MIT

---

Created by Mike Kozub