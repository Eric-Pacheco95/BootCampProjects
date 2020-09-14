var svgWidth = 960;
var svgHeight = 500;

var margin = {
    top: 50,
    right: 50,
    bottom: 80,
    left: 50
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3.select("#svg-area")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Import Data
d3.csv("assets/data/data.csv").then(function (data) {
    povertyPercentages = []
    healthcareNumbers = []
    data.forEach(state => {
        state.poverty = +state.poverty;
        povertyPercentages.push(state.poverty);
        state.healthcare = +state.healthcare
        healthcareNumbers.push(state.healthcare);
    })
    // Create scale functions for x and y axis
    var xLinearScale = d3.scaleLinear()
        .domain([d3.min(povertyPercentages)-1, d3.max(povertyPercentages)+1])
        .range([0, width]);

    var yLinearScale = d3.scaleLinear()
        .domain([d3.min(healthcareNumbers) - 1, d3.max(healthcareNumbers)])
        .range([height, 0]);

    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // Append axis to charts
    chartGroup.append("g")
        .attr("transform", `translate(0, ${height})`)
        .call(bottomAxis)

    chartGroup.append("g")
        .call(leftAxis);
    
    //Label x and y Axis
    chartGroup.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left)
        .attr("x", 0 - (height / 1.5))
        .attr("dy", "1em")
        .attr("class", "axisText")
        .text("Lacks Healthcare %");

    chartGroup.append("text")
        .attr("transform", `translate(${width / 2}, ${height + margin.top})`)
        .attr("class", "axisText")
        .text("In Poverty %");

    // Create circles
    var circles = chartGroup.selectAll("circle")
        .data(data)
        .enter()
        .append("circle")
        .attr("cx",function(d) {
            return xLinearScale(d.poverty)
        })
        .attr("cy", function (d) {
            return yLinearScale(d.healthcare)
        })
        .attr("r", "15")
        .attr("fill", "pink")
        .attr("opacity", ".5")
    
    // Label circles

    chartGroup.append('g')
    .selectAll('text')
    .data(data)
    .enter()
    .append('text')
    .attr('x',d => xLinearScale(d.poverty)-5)
    .attr('y', d => yLinearScale(d.healthcare)+4)
    .text(d => d.abbr)
    .attr('font-size','8px')
});