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

// function getElementInfo(layerName){
//   map.on('singleclick', function (evt) {
//     var viewResolution = /** @type {number} */ (view.getResolution());
//     var url = layerName.getSource().getFeatureInfoUrl(
//       evt.coordinate,
//       viewResolution,
//       'EPSG:3857',
//       {
//         'INFO_FORMAT': 'application/json'
//       }
//     );
//     if (url) {
//       // console.log(url);
//       fetch(url)
//         .then((response) => response.json())
//         .then((data) => {
//           properties = data.features[0].properties;
//           console.log(properties);
//         });
//     }
//   });
// };


function getElementInfo(layerName, layerTitle){
  map.on('singleclick', function (event) {
    var viewResolution = view.getResolution();
    var coordinates = event.coordinate;
    var epsg = 'EPSG:3857';
    var params = {
        'INFO_FORMAT': 'application/json'
      };
    var url = layerName.getSource().getFeatureInfoUrl(
      coordinates,
      viewResolution,
      epsg,
      params,
    );
    console.log(url);
    async function getFeatureProperties() {
      try {
        var response = await fetch(url);
        if (!response.ok) {
          throw new Error(`HTTP error!\n Status: ${response.status}\n Type: ${response.type}\n URL: ${response.url}`);
        } else {
          var data = await response.text();
          var json = JSON.parse(data).features[0].properties;
          // console.log(json);

          var tableHeadContents = '<thead>'
          + '<tr><th colspan="2">' + layerTitle + '</th></tr>'
          // + '<tr><th>#</th><th>Info</th></tr>'
          + '</thead>';
          var tableHead = $(tableHeadContents).attr("id","thead");
          console.log(tableHeadContents);
          $("#onclickinfo").append(tableHead);
          var tableBodyContents = '<tbody></tbody>';
          var tableBody = $(tableBodyContents).attr("id","tbody");
          console.log(tableBody);
          $("#onclickinfo").append(tableBody);
          for (items in json) {
            key = items;
            value = json[items];
            // elementData = [key, value];
            // console.log(elementData);
            tableRow = '<tr><td class="td-head">' + key + '</td><td class="td-body">' + value + '</td></tr>';
            console.log(tableRow);
            $("tbody").append(tableRow);
          }

        }
      } catch (e) {
        console.log(e);
      }
    }
    getFeatureProperties();
  });
};

function getElementLegend(layerName) {
  var updateLegend = function(resolution) {
    var params = {
        'INFO_FORMAT': 'application/json'
      };
    var url = layerName.getSource().getLegendUrl(resolution, params);
    async function getFeatureProperties() {
      try {
        var response = await fetch(url);
        console.log(response);
        // if (!response.ok) {
        //   throw new Error(`HTTP error!. Status: ${response.status}`);
        // } else {
        //   var data = await response.text();
        //   var legendJSON = JSON.parse(data).Legend[0];
        //   console.log(legendJSON);
        //   // /// Lettura colormap se è presente
        //   // var legendData = legendJSON.rules[0].symbolizers[0].Raster.colormap.entries;
        //   // // if (legendData !== 'undefined') {
        //   // //   /// Creazione del div che conterrà la legenda
        //   // //   var divLegend = $("<div/>").attr("id","indexLegend");
        //   // //   $("#legend").append(divLegend);
        //   // //   arrayColors = [];
        //   // //   arrayLabels = [];
        //   // //   for (items in legendData){
        //   // //     colors = legendData[items]["color"]
        //   // //     arrayColors.push(colors);
        //   // //
        //   // //     labels = legendData[items]["label"]
        //   // //     arrayLabels.push(labels);
        //   // //   }
        //   // //   var divLabelFirst = '<div class="legend-info">' + arrayLabels[0] + '</div>'
        //   // //   var divColor = '<div class="legend-colormap" style="background-image: linear-gradient(to right, ' + arrayColors + ');"></div>'
        //   // //   var divLabelLast = '<div class="legend-info">' + arrayLabels[arrayLabels.length - 1] + '</div>'
        //   // //   $("#indexLegend").html('');
        //   // //   $("#indexLegend").append('<div class="legend-contents" id="">' + divLabelFirst + divColor + divLabelLast + '</div>')
        //   // // } else {
        //   // //   console.error('legendData is undefined!');
        //   // // }
        // }
      } catch (e) {
        console.log(e);
      }
    }
    getFeatureProperties();
  };
  /// Inizializzazione della legenda
  var viewResolution = view.getResolution();
  updateLegend(viewResolution);
  // /// Aggiornamento della legenda al variare della risoluzione
  // map.getView().on('change:resolution', function(event) {
  //   var resolution = event.target.getResolution();
  //   updateLegend(resolution);
  // });
};
