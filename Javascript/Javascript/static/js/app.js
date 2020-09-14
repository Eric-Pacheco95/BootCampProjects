// from data.js
// YOUR CODE HERE!

// Grab html elements needed
var tableData = data;
var form = d3.select('form');
var form_button = d3.select('.btn-default');
var ufo_tbody = d3.select('#ufo_body');

// Add data to ufo-table
data.forEach(input => {
    var row = ufo_tbody.append("tr");
    Object.entries(input).forEach(([key,value]) => {
        row.append('td').text(value);
    })
}) 

// Set-up filter search form to show data from desired dates
function searchDate(date) {
    // Prevent the page from refreshing
    d3.event.preventDefault();
    
    // Select form input and get date
    var inputElement = d3.select("#datetime");

    var inputValue = inputElement.property("value");

    // Clear all data from the HTML table
    ufo_tbody.html('')

    // Search data according to input date and fill HTML table
    // If statement checks if nothing was entered into form. If nothing is entered, the table is reset to show all data
    if(inputValue === '') {
        data.forEach(input => {
            var row = ufo_tbody.append("tr");
            Object.entries(input).forEach(([key,value]) => {
                row.append('td').text(value);
            })
        }) 
    }
    else {
        data.forEach(x => {
            if(x.datetime === inputValue) {
                var row = ufo_tbody.append("tr");
                Object.entries(x).forEach(([key,value]) => {
                    row.append('td').text(value);
                })
            }
        })
    }
}

// Event Handlers for enter or clicking filter table
form_button.on("click", searchDate);
form.on("submit", searchDate);
