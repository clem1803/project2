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


d3.json("WWI_aerial_attack_data.json").then(function(response) {

  console.log(response);

  var markers = [];

  for (var i = 0; i < response.length; i++) {
    var location = [response[i].LATITUDE, response[i].LONGITUDE];

    if (location) {
      markers.push(location);
    }
  }

  var dots = L.marker(markers, {
    // radius: 50,
    // blur: 35
  }).addTo(myMap);

}).catch(function(error) {
    console.log(error);
});
