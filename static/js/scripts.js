// static/js/scripts.js
document.addEventListener("DOMContentLoaded", function() {
    console.log("Scripts loaded successfully!");
    // You can add your JavaScript logic here.
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// Add an event listener for the signup form submission
const signupForm = document.querySelector('#signup-form'); // Assuming the form has an ID
if (signupForm) {
    signupForm.addEventListener('submit', async (e) => {
        e.preventDefault(); // Prevent default form submission
        const formData = new FormData(e.target);
        const formObject = Object.fromEntries(formData.entries());

        const response = await fetch('/api/signup/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken  // Add CSRF token to the request header
            },
            body: JSON.stringify(formObject),
        });

        if (response.ok) {
            const data = await response.json();
            alert(data.message || 'Sign up successful!');
        } else {
            const error = await response.json();
            alert(error.error || 'Something went wrong.');
        }
    });
}
