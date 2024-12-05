document.getElementById("prediction-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    
    fetch('/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        window.location.href = `result.html?result=${data}`;
    })
    .catch(error => console.error('Error:', error));
});
