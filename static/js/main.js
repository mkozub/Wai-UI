// Recents modal functionality
function showRecents() {
    const modal = document.getElementById('recentsModal');
    modal.style.display = 'flex';
}

function closeRecents() {
    const modal = document.getElementById('recentsModal');
    modal.style.display = 'none';
}

// Form validation
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.input-form');
    if (form) {
        form.addEventListener('submit', function(event) {
            // Basic validation example - you can expand this as needed
            const zipCode = document.getElementById('location').value.trim();
            const zipCodeRegex = /^\d{5}$/;
            
            if (!zipCodeRegex.test(zipCode)) {
                event.preventDefault();
                alert('Please enter a valid 5-digit zip code.');
                return;
            }
        });
    }
});

// Responsive element adjustments
function adjustResponsiveElements() {
    const width = window.innerWidth;
    const buttonText = document.querySelectorAll('.button-text');
    
    if (width < 480) {
        // On very small screens, make buttons more compact
        buttonText.forEach(text => {
            text.style.fontSize = '0.9rem';
        });
    } else {
        buttonText.forEach(text => {
            text.style.fontSize = '1rem';
        });
    }
}

// Run on load and resize
window.addEventListener('load', adjustResponsiveElements);
window.addEventListener('resize', adjustResponsiveElements);

// Escape key to close modals
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeRecents();
    }
});

// Close modal when clicking outside of modal content
window.addEventListener('click', function(event) {
    const modal = document.getElementById('recentsModal');
    if (event.target === modal) {
        closeRecents();
    }
});
