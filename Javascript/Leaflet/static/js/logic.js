//Initialize map
var myMap = L.map('map', {
    center: [39.83, -98.58],
    zoom: 4
});

// Add tile layer from mapbox
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "light-v10",
    accessToken: API_KEY
}).addTo(myMap);

//Add Legend
var legend = L.control({position: 'bottomright'});

legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = [0,1,2,3,4,5];
        

    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(grades[i]) + '"></i> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    }

    return div;
};

legend.addTo(myMap);

var earthquakeUrl = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson';

//Get Corresponding color based on magnitude of earthquake
function getColor(magnitude) {
    var color = '';
    if (magnitude > 5) {
        color = '#800026'
    }
    else if (magnitude > 4) {
        color = '#BD0026'
    }
    else if (magnitude > 3) {
        color = '#E31A1C' 
    }
    else if (magnitude > 2) {
        color = '#FC4E2A'
    }
    else if (magnitude > 1) {
        color = '#FD8D3C'
    }
    else {
        color = '#FEB24C'
    }
    return color
}

d3.json(earthquakeUrl, data => {
    data.features.forEach(earthquake => {
        var magnitude = earthquake.properties.mag;
        var color = getColor(magnitude)
        L.circleMarker([earthquake.geometry.coordinates[1], earthquake.geometry.coordinates[0]], {
            fillOpacity: 0.75,
            color: color,
            radius: Math.pow(magnitude,2)
        }).bindPopup("<h1>" + earthquake.properties.title + "</h1> <hr> <h3>Magnitude: " + magnitude + "</h3>").addTo(myMap)
    })
})
