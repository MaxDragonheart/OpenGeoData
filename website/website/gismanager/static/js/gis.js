function createBBoxLayer(bboxCoordinates, bboxName){

  // Build the vector
  coordinates = [[
    [bboxCoordinates[0], bboxCoordinates[1]],
    [bboxCoordinates[0], bboxCoordinates[3]],
    [bboxCoordinates[2], bboxCoordinates[3]],
    [bboxCoordinates[2], bboxCoordinates[1]],
    [bboxCoordinates[0], bboxCoordinates[1]],
  ]];
  polygon = new ol.Feature(
    new ol.geom.Polygon(coordinates).transform('EPSG:4326','EPSG:3857')
  );
  bbox = new ol.layer.Vector({
    title: bboxName,
    source: new ol.source.Vector({
        features: [polygon]
    }),
    opacity: 0
  });

  return bbox;

};

function zoomOnLayer(
  layerName,
  paddingTop,
  paddingLeft,
  paddingBottom,
  paddingRight,
  durationMilliseconds
){

  var extent = layerName.getSource().getExtent();
  var options = {
    size: map.getSize(),
    padding: [paddingTop, paddingLeft, paddingBottom, paddingRight],
    duration: durationMilliseconds
  }
  map.getView().fit(extent, options);

};

function layerOpacity(layerName, elementID, outputID){
  var control = document.getElementById(elementID);
  var output = document.getElementById(outputID);
  var listener = function () {
    output.innerText = control.value;
    layerName.setOpacity(control.value / 100);
  };
  control.addEventListener('input', listener);
  control.addEventListener('change', listener);
  output.innerText = control.value;
  layerName.setOpacity(control.value / 100);
};
