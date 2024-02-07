const refreshInterval = 10000; // 10 seconds
// Function to refresh the page
function refreshPage() {
    location.reload();
}

// Schedule the page refresh
setTimeout(refreshPage, refreshInterval);

// First, retrieve the lastData value using an AJAX request
$.get('/get_last_data', function(data) {
    // 'data' contains the value of last_data
    var lastData = data;

    // Now you can use 'lastData' in your client-side JavaScript
    console.log('Last data:', lastData);

    // Make another AJAX request to retrieve user data
    fetch("http://127.0.0.1:5000/user/getall")
        .then((response) => {
            return response.json();
        })
        .then((userData) => {
            console.log(userData[lastData].balance);

            // Delay the blacklisted condition check by 3 seconds
            setTimeout(function() {
                if (userData[lastData].blacklisted_tag === 0) {
                    alert('Payment Received');
                } else if (userData[lastData].blacklisted_tag === 1) {
                    alert('Payment Not Received');
                }
            }, 3000);

            // Construct the HTML for displaying user data
            let tabledata = `<label for="datascience">Balance</label><br>
                <input type="text" id="balance" name="datascience" value=${userData[lastData].balance}><br><br>
                <label for="id">ID:</label><br>
                <input type="text" id="id" name="science" value=${userData[lastData].id}><br>
                <label for="class">Vehicle Class:</label><br>
                <input type="text" id="class" name="maths" value=${userData[lastData].vehicle_class}><br><br>
                <label for="vehicleno">Vehicle Number</label><br>
                <input type="text" id="vehicleno" name="c" value="${userData[lastData].vehicle_no}"><br><br>
                <label for="datascience">Blacklisted Tag</label><br>
                <input type="text" id="datascience" name="datascience" value=${userData[lastData].blacklisted_tag}><br><br>
                <label for="datascience">Vehicle Weight</label><br>
                <input type="text" id="weight" name="datascience" value=${userData[lastData].vehicle_weight}><br><br>
                <label for="datascience">Balance</label><br>
                <input type="text" id="balance" name="datascience" value=${userData[lastData].balance}><br><br>
            </div>`;

            // Update the HTML element with the generated tabledata
            document.getElementById('hello').innerHTML = tabledata;
        });
});
