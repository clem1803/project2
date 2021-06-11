var myMap = L.map("map", {
  center: [39.8283, -98.5795],
  zoom: 4
});

L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 1000,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: "pk.eyJ1IjoiY2xlbTE4MDMiLCJhIjoiY2twNGszc25vMjFmdDJ1cXdjZzFuMTNvMSJ9.Z9LOJ7Q_Z18Srpymu_xqEw"
}).addTo(myMap);


d3.json("/api/v1.0/aerial_attack").then(function(response) {

  console.log(response);

  var marker = [];

  for (var i = 0; i < response.length; i++) {
    var location = [response[i].LATITUDE, response[i].LONGITUDE];

    if (location) {
      heatArray.push(location);
    }
  }

  var heat = L.heatLayer(heatArray, {
    radius: 50,
    blur: 35
  }).addTo(myMap);

}).catch(function(error) {
    console.log(error);
});
