document.getElementById('inputForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Collect the user input values into different constants
    const inputValue0 = parseFloat(document.getElementById('input0').value);
    const inputValue1 = parseFloat(document.getElementById('input1').value);
    const inputValue2 = parseFloat(document.getElementById('input2').value);
    const inputValue3 = parseFloat(document.getElementById('input3').value);

    // Convert the user input values into a 2D array to use in the NN model
    const data = {
        inputs: [inputValue0, inputValue1, inputValue2, inputValue3]
    };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('latitude-result').innerText = 'Error: ' + data.error;
        } else {
            document.getElementById('latitude-result').innerText = data.prediction;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('latitude-result').innerText = 'Error outputting results';
    });
});
