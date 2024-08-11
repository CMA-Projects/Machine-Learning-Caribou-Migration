document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent default form submission

    const month = parseFloat(document.getElementById('month').value);
    const temperature = parseFloat(document.getElementById('temperature').value);
    const day = parseFloat(document.getElementById('day').value);

    // Send the data to the Flask backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ month: month, temperature: temperature, day: day })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Display the result
        document.getElementById('latitude').textContent = 'Latitude: ' + data.latitude;
        document.getElementById('results').style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
