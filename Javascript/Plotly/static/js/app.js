function buildMetadata(sample) {
    // Use `d3.json` to fetch the metadata for a sample
    var url = `/metadata/${sample}`
    d3.json(url).then(metadata => {

        var metadata_panel=d3.select("#sample-metadata")
        // Use `.html("") to clear any existing metadata
        metadata_panel.html("")

        Object.entries(metadata).forEach(([key,value]) => {
            metadata_panel.append('p').append('span').text(`${key} : ${value.toString()}`)
        })
        // Build the Gauge Chart
        var level= (metadata.wfreq+1)*18-9

        // Trig to calc meter point
        var degrees = 180 - level,
        radius = .5;
        var radians = degrees * Math.PI / 180;
        var x = radius * Math.cos(radians);
        var y = radius * Math.sin(radians);

        var mainPath = 'M -.0 -0.025 L .0 0.025 L ',
        pathX = String(x),
        space = ' ',
        pathY = String(y),
        pathEnd = ' Z';
        var path = mainPath.concat(pathX,space,pathY,pathEnd);

        var data = [{ type: 'scatter',
        x: [0], y:[0],
        marker: {size: 28, color:'850000'},
        showlegend: false,
        name: 'Wash Frequency',
        text: level,
        hoverinfo: 'name'},
        { values: [50/9, 50/9, 50/9, 50/9, 50/9, 50/9, 50/9, 50/9, 50/9, 50],
        direction: "clockwise",
        rotation: 90,
        text: ['0-1', '1-2', '2-3', '3-4','4-5','5-6', '6-7', '7-8', '8-9', ''],
        textinfo: 'text',
        textposition:'inside',
        marker: {colors:['rgba(230, 255, 255, .5)', 
                        'rgba(204, 255, 255, .5)',
                        'rgba(179, 255, 255, .5)',
                        'rgba(153, 255, 255, .5)',
                        'rgba(128, 255, 255, .5)',
                        'rgba(102, 255, 255, .5)',
                        'rgba(77, 255, 255, .5)',
                        'rgba(51, 255, 255, .5)',
                        'rgba(26, 255, 255, .5)',
                        'rgba(255, 255, 255, 0)']},
        labels: ['0-1', '1-2', '2-3', '3-4','4-5','5-6', '6-7', '7-8', '8-9', ''],
        hoverinfo: 'label',
        hole: .5,
        type: 'pie',
        showlegend: false
        }];

        var layout = {
        title: "Belly Button Washing Frequency",
        shapes:[{type: 'path', path: path, fillcolor: '850000', line: {color: '850000'}}],
        xaxis: {zeroline:false, showticklabels:false,
                showgrid: false, range: [-1, 1]},
        yaxis: {zeroline:false, showticklabels:false,
                showgrid: false, range: [-1, 1]},
        height: 500,
        width: 500
        };

        Plotly.newPlot('gauge', data, layout);
    })
};

function buildChart(sample) {
    // Use `d3.json` to fetch the sample data for a sample
    var url = `/samples/${sample}`
    d3.json(url).then(sampleData => {

        //Grab sample_values, otu_ids, otu_labels as variables
        var sampleValues = sampleData.sample_values;
        var otuIds = sampleData.otu_ids;
        var otuLabels = sampleData.otu_labels;

        //Grab top 10 OTUs and reverse them to show top value at top of bar chart
        var samplesValuesReversed = sampleValues.slice(0,10).reverse()
        var otuIdsReversed = otuIds.slice(0,10).reverse()
        var otuLabelsReversed = otuLabels.slice(0,10).reverse()
        // otu_ids must be a string or else the y axis will be spread out based on the otu_ids integer value
        var otuIdsReversedStrings = otuIdsReversed.map(id => id.toString()).map(id => 'OTU '.concat(id))
        
        //Make Bar Chart
        var trace1 = {
            type: 'bar',
            x: samplesValuesReversed,
            y: otuIdsReversedStrings,
            orientation: 'h',
            text:otuLabelsReversed
        };

        var data1 = [trace1]

        var layout1 = {
            title: `Top 10 OTUs for sample ${sample}`,
            yaxis: {title: 'otu_ids'},
            xaxis: {title: 'sample values'},
            height: 500,
            width: 500
        };
        
        Plotly.newPlot('bar',data1,layout1)

        //Make Bubble Chart
        var trace2 = {
            x:otuIds,
            y:sampleValues,
            text:otuLabels,
            mode:'markers',
            marker:{
                size:sampleValues,
                color:otuIds
            },
            hoverinfo:'text + x + y'
        };

        var data2 = [trace2];

        var layout2 = {
            title:`Top 10 OTUs for sample ${sample}`,
            xaxis: {title:'otu id'},
            yaxis:{title:'sample value'},
            height: 500,
            width: 1000
        }

        Plotly.newPlot('bubble',data2,layout2);

    });
};

//Build new charts when dropdown selection is made
function optionChanged(sample) {
    buildMetadata(sample);
    buildChart(sample);
}

function initDashboard() {
    var dropDown = d3.select('#selDataset');

    //Fill Dropdown Menu
    d3.json('/names').then(names => {
        var Names = names.names
        dropDown.selectAll('option')
        .data(Names)
        .enter()
        .append('option')
        .text(name => name)
        
        //Fill Metadata & Charts with first sample info
        var firstSample = Names[0];
        buildMetadata(firstSample);
        buildChart(firstSample);
    });
}

initDashboard()


