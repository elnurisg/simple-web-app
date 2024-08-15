document.getElementById('calculateButton').addEventListener('click', function() {
    const number1 = document.getElementById('number1').value;
    const number2 = document.getElementById('number2').value;
    const operation = document.getElementById('operation').value;

    const data = {
        a: parseInt(number1),
        b: parseInt(number2),
        operation: operation
    };

    fetch('http://localhost:8000/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('result').innerText = `Result: ${result.result}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'An error occurred.';
    });
});

document.getElementById('infoButton').addEventListener('click', function() {
    const description = document.getElementById('description');
    description.classList.toggle('visible');
});
