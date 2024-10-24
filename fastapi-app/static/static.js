document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('form').addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission

        const form = event.target;
        const formData = new FormData(form);

        fetch('/predictionForm', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(prediction => {
            document.getElementById('prediction').innerHTML = '<p>' + prediction + '</p>';
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
