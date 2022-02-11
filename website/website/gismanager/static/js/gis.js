let map;
let view;

function MapInizialized(mapTarget) {
  /*
  This function initialize the map
  mapTarget: string. It is the id of the div that contain the map.
  */
  map = new ol.Map({
    target: mapTarget,
    controls: ol.control.defaults({
      attribution: false,
      // zoom: false,
    }),
  });

  return map;
};

function MapZoomControl() {
  /* TODO
  This function allow the use of custom
  zoom-in and zoom-out
  */
};

function MapScaleLine() {
  /*
  This function define the scale line.
  */
  const scaleLine = new ol.control.ScaleLine({
    className: 'ol-scale-line',
    target: document.getElementById('scale-line')
  });
  map.addControl(scaleLine);

  return scaleLine;
};

function MapFullScreen() {
  /*
  This function allow to have the full screen map
  */
  const fullScreen = new ol.control.FullScreen({
    className: 'ol-full-screen',
    tipLabel: 'Toggle full-screen'
  });
  map.addControl(fullScreen);

  return fullScreen;
};

function MapAttribution() {
  const attribution = new ol.control.Attribution({
    className: 'ol-attribution',
    label: 'a',
    collapsible: true,
    collapsed: true,
    target: document.getElementById('map-attribution'),
  });
  map.addControl(attribution);

  return attribution;
};

function MapSetView(longitude, latitude, zoomLevel, setMaxZoom, setMinZoom) {
  /*
  This function define the initial view of the map.
  longitude: decimal. It is the longitude of the initial center of the map.
  latitude: decimal. It is the latitude of the initial center of the map.
  zoomLevel: decimal. It is the inizial zoom of the map.
  setMaxZoom: decimal. It is the max zoom of the map.
  setMinZoom: decimal. It is the min zoom of the map.
  */
  view = new ol.View({
    center: ol.proj.fromLonLat([longitude, latitude]),
    zoom: zoomLevel,
    maxZoom: setMaxZoom,
    minZoom: setMinZoom
  });
  map.setView(view);

  return view;
};

function baseMapLayer(
  // baseMapName,
  // attribution,
  // mapbox_user,
  // mapbox_token
) {
  /*
  This function define the base map.
  It is possibile to create an empty map or a Tile based on OSM.
  baseMapName: string. It is the name of the Tile.
  */
  let empty;
  let osm;

  return {
    'createEmpty': function() {
      /*
      Empty basemap.
      */
      const empty = new ol.layer.Tile({
        title: 'Empty Map',
        source: new ol.source.XYZ(),
        zIndex: 0
      });
      return empty;
    },
    'createOSMStandard': function(
      baseMapName,
    ) {
      /*
      Basemap based on Open Street Map.
      */
      this.baseMapName = baseMapName;

      let osm = new ol.layer.Tile({
        title: baseMapName,
        source: new ol.source.OSM(),
        zIndex: 0
      });
      return osm;
    },
    'createMapBoxTileV1': function(
      baseMapName,
      attribution,
      mapbox_user,
      mapbox_tile_code,
      mapbox_token
    ) {
      /*
      Basemap based on MapBox Studio
      */
      this.baseMapName = baseMapName;
      this.attribution = attribution;
      this.mapbox_user = mapbox_user;
      this.mapbox_tile_code = mapbox_tile_code;
      this.mapbox_token = mapbox_token;

      let mapboxStudio = new ol.layer.Tile({
        title: baseMapName,
        source: new ol.source.XYZ({
            attributions: attribution,
            url: 'https://api.mapbox.com/styles/v1/' + mapbox_user + '/'
                + '' + mapbox_tile_code + '/tiles/256/{z}/{x}/{y}?'
                + 'access_token=' + mapbox_token + ''
          }),
        zIndex: 0,
        // opacity: setOpacity
      });
      return mapboxStudio;
    },
  }

};

function zoomOnCoordinates(arrayCoordinates) {

  clickedPoint = ol.proj.fromLonLat(arrayCoordinates)

  function flyTo(location, done) {
    const duration = 2000;
    const zoom = 16;
    let parts = 2;
    let called = false;
    function callback(complete) {
      --parts;
      if (called) {
        return;
      }
      if (parts === 0 || !complete) {
        called = true;
        done(complete);
      }
    }
    view.animate(
      {
        center: location,
        duration: duration,
      },
      callback
    );
    view.animate(
      {
        zoom: 8,
        duration: duration / 2,
      },
      {
        zoom: zoom,
        duration: duration,
      },
      callback
    );
  }
  flyTo(clickedPoint, function () {});

};

let vectorsLayer = function(
  vectorType,
  urlAPI,
  vectorsLayerName
){
  /*
  This function allow to visualize vectors on
  the map.
  vectorType: string. It can be point, linestring and polygon.
  urlAPI: string. It is the path to the single vector resource in ol.format.GeoJSON format. It' possibile
        to use also an API's url.
  vectorsLayerName: string. It is the name of the vector resource.
  */
  this.vectorType = vectorType;
  this.urlAPI = urlAPI;
  this.vectorsLayerName = vectorsLayerName;

  let layerVector;

  return {
    'createVector': function(
      setStrokeColor,
      setStrokeLineDashLength,
      setStrokeLineDashSpace,
      setStrokeWidth,
      setFillColor,
      setMaxZoom,
      setMinZoom,
      setZIndex,
      setOpacity
    ){
      /*
      This function create the vector resource.
      setStrokeColor: string. It's the rgba color.
      setStrokeLineDashLength: decimal. It's a number that define the length of the dash. It's can be null.
      setStrokeLineDashSpace: decimal. It's a number that define the space between the dashes. It's can be null.
      setStrokeWidth: integer. This number define the stroke line's width.
      setFillColor: string. It's the rgba color.
      setMaxZoom: decimal. It's the max zoom level with which is possible to see the vector.
      setMinZoom decimal. It's the min zoom level with which is possible to see the vector.
      setZIndex: integer. It's the the level priority for the vector. The higher it is, the higher the position
                of the vector in the stack of layers.
      */
      this.setStrokeColor = setStrokeColor;
      this.setStrokeLineDashLength = setStrokeLineDashLength;
      this.setStrokeLineDashSpace = setStrokeLineDashSpace;
      this.setStrokeWidth = setStrokeWidth;
      this.setFillColor = setFillColor;
      this.setMaxZoom = setMaxZoom;
      this.setMinZoom = setMinZoom;
      this.setZIndex = setZIndex;
      this.setOpacity = setOpacity;

      let stroke, fill;
      // Vector's style definition.
      stroke = new ol.style.Stroke({
          color: setStrokeColor,
          width: setStrokeWidth,
          lineDash: [setStrokeLineDashLength, setStrokeLineDashSpace],
          lineCap: 'butt',
          lineJoin: 'miter'
      });
      fill = new ol.style.Fill({
        color: setFillColor,
      });

      let style;
      // Change style based on the geometry type.
      if (vectorType.toLowerCase() === 'polygon') {
        style = new ol.style.Style({
            stroke: stroke,
            fill: fill
        });
      } else if (vectorType.toLowerCase() === 'linestring') {
        style = new ol.style.Style({
            stroke: stroke
        });
      } else if (vectorType.toLowerCase() === 'point') {
        style = new ol.style.Style({
            image: new ol.style.Circle({
              radius: setStrokeWidth * 5,
              stroke: stroke,
              fill: fill
            })
        });
      } else {
        console.error('Geometry not recognized! Accepted geometries: point, linestring, polygon.');
      }
      // Build the vector
      layerVector = new ol.layer.Vector({
        title: vectorsLayerName,
        source: new ol.source.Vector({
            url: urlAPI,
            format: new ol.format.GeoJSON(),
        }),
        style: style,
        minZoom: setMinZoom,
        maxZoom: setMaxZoom,
        zIndex: setZIndex,
        opacity: setOpacity
      });
      return layerVector;
    },
    'zoomToExtent': function(
      paddingTop,
      paddingLeft,
      paddingBottom,
      paddingRight,
      durationMilliseconds
    ){
      /*
      This function allow to zoom on the target vector's extent.
      paddingTop: integer. It is the top padding.
      paddingLeft: integer. It is the left padding.
      paddingBottom: integer. It is the bottom padding.
      paddingRight: integer. It is the right padding.
      durationMilliseconds: integer. Corresponds to how long the zoom lasts.
      */
      this.paddingTop = paddingTop;
      this.paddingLeft = paddingLeft;
      this.paddingBottom = paddingBottom;
      this.paddingRight = paddingRight;
      this.durationMilliseconds = durationMilliseconds;

      layerVector.getSource().once('change', function(evt) {
        if (layerVector.getSource().getState() === 'ready') {
          if (layerVector.getSource().getFeatures().length > 0) {
            const extent = layerVector.getSource().getExtent();
            const options = {
              size: map.getSize(),
              padding: [paddingTop, paddingLeft, paddingBottom, paddingRight],
              duration: durationMilliseconds
            }
            map.getView().fit(extent, options);
          }
        }
      });
    },
    'zoomOnLayer': function(
      paddingTop,
      paddingLeft,
      paddingBottom,
      paddingRight,
      durationMilliseconds
    ){
      /*
      This function activates the zoom by clicking on the button.
      paddingTop: integer. It is the top padding.
      paddingLeft: integer. It is the left padding.
      paddingBottom: integer. It is the bottom padding.
      paddingRight: integer. It is the right padding.
      durationMilliseconds: integer. Corresponds to how long the zoom lasts.
      */
      this.paddingTop = paddingTop;
      this.paddingLeft = paddingLeft;
      this.paddingBottom = paddingBottom;
      this.paddingRight = paddingRight;
      this.durationMilliseconds = durationMilliseconds;

      const extent = layerVector.getSource().getExtent();
      const options = {
        size: map.getSize(),
        padding: [paddingTop, paddingLeft, paddingBottom, paddingRight],
        duration: durationMilliseconds
      }
      map.getView().fit(extent, options);
    },
    'lockToExtent': function(
      paddingTop,
      paddingLeft,
      paddingBottom,
      paddingRight
    ){
      /*
      This function activates lock on the vector's target extent.
      paddingTop: integer. It is the top padding.
      paddingLeft: integer. It is the left padding.
      paddingBottom: integer. It is the bottom padding.
      paddingRight: integer. It is the right padding.
      */
      this.paddingTop = paddingTop;
      this.paddingLeft = paddingLeft;
      this.paddingBottom = paddingBottom;
      this.paddingRight = paddingRight;

      layerVector.getSource().once('change', function(evt) {
        if (layerVector.getSource().getState() === 'ready') {
          if (layerVector.getSource().getFeatures().length > 0) {
            const extent = layerVector.getSource().getExtent();
            const options = {
              size: map.getSize(),
              padding: [paddingTop, paddingLeft, paddingBottom, paddingRight],
            }
            map.getView().fit(extent, options);

            const newView = new View({
              extent: extent,
              showFullExtent: true,
              center: map.getView().getCenter(),
              zoom: map.getView().getZoom()
            });
            map.setView(newView);
          }
        }
      });
    },
    'createCluster': function(
      clusterDistance,
      colorMaxCluster,
      colorMiddleCluster,
      colorMinCluster,
      colorUncluster,
      setStrokeColorCluster,
      setStrokeLineDashLengthCluster,
      setStrokeLineDashSpaceCluster,
      setStrokeWidthCluster,
      colorTextCluster,
      setMaxZoom,
      setMinZoom,
      setZIndex
    ){
      /*
      This function allow to create the clusters from points' vector.
      clusterDistance: integer. Define the distance buffer useful for points' aggregation.
      colorMaxCluster: string. It's the rgba color of the biggest cluster.
      colorMiddleCluster: string. It's the rgba color of the intermediate cluster.
      colorMinCluster: string. It's the rgba color of the smaller cluster.
      colorUncluster: string. It's the rgba color of the unclustered point.
      setStrokeColorCluster: string. It's the rgba color.
      setStrokeLineDashLengthCluster: decimal. It's a number that define the length of the dash. It's can be null.
      setStrokeLineDashSpaceCluster: decimal. It's a number that define the space between the dashes. It's can be null.
      setStrokeWidthCluster: integer. This number define the stroke line's width.
      colorTextCluster: string. It's the rgba color.
      setMaxZoom: decimal. It's the max zoom level with which is possible to see the vector.
      setMinZoom decimal. It's the min zoom level with which is possible to see the vector.
      setZIndex: integer. It's the the level priority for the vector. The higher it is, the higher the position
                of the vector in the stack of layers.
      */
      this.clusterDistance = clusterDistance;
      this.colorMaxCluster = colorMaxCluster;
      this.colorMiddleCluster = colorMiddleCluster;
      this.colorMinCluster = colorMinCluster;
      this.colorUncluster = colorUncluster;
      this.setStrokeColorCluster = setStrokeColorCluster;
      this.setStrokeLineDashLengthCluster = setStrokeLineDashLengthCluster;
      this.setStrokeLineDashSpaceCluster = setStrokeLineDashSpaceCluster;
      this.setStrokeWidthCluster = setStrokeWidthCluster;
      this.colorTextCluster = colorTextCluster;
      this.setMaxZoom = setMaxZoom;
      this.setMinZoom = setMinZoom;
      this.setZIndex = setZIndex;

      // ol.source.Cluster's style definition
      let styleCache = {};
      function getStyle (feature, resolution) {
        let size = feature.get('features').length;
        let style = styleCache[size];

        if (!style) {
          let color = size>clusterDistance ? colorMaxCluster : size>clusterDistance/3 ? colorMiddleCluster : size>1 ? colorMinCluster : colorUncluster;
          let radius = Math.max(8, Math.min(size*1.5, 20));
          style = styleCache[size] = new ol.style.Style({
            image: new ol.style.Circle({
              radius: radius*1.5,
              stroke: new ol.style.Stroke({
                color: setStrokeColorCluster,
                width: setStrokeWidthCluster,
                lineDash: [setStrokeLineDashLengthCluster, setStrokeLineDashSpaceCluster],
              }),
              fill: new ol.style.Fill({
                color: color
              })
            }),
            text: new ol.style.Text({
              scale: radius/8,
              text: size.toString(),
              fill: new ol.style.Fill({
                color: colorTextCluster
              }),
              textAlign: 'center',
              textBaseline: 'middle'
            })
          });
        }
        return style;
      };

      // Build the cluster vector
      layerVector = new ol.layer.Vector({
        title: vectorsLayerName,
        source: new ol.source.Cluster({
          source: new ol.source.Vector({
              url: urlAPI,
              format: new ol.format.GeoJSON(),
          }),
          distance: clusterDistance
        }),
        style: getStyle,
        minZoom: setMinZoom,
        maxZoom: setMaxZoom,
        zIndex: setZIndex
      });
      return layerVector;
    },
    'zoomOnCluster': function(
      paddingTop,
      paddingLeft,
      paddingBottom,
      paddingRight,
      durationMilliseconds
    ){
      /*
      This function activates zoom on clusters. The function is inactive for
      the unclustered points.
      paddingTop: integer. It is the top padding.
      paddingLeft: integer. It is the left padding.
      paddingBottom: integer. It is the bottom padding.
      paddingRight: integer. It is the right padding.
      durationMilliseconds: integer. Corresponds to how long the zoom lasts.
      */
      this.paddingTop = paddingTop;
      this.paddingLeft = paddingLeft;
      this.paddingBottom = paddingBottom;
      this.paddingRight = paddingRight;
      this.durationMilliseconds = durationMilliseconds;

      map.on('singleclick', function(event) {
        const feature = map.forEachFeatureAtPixel(event.pixel, function(feature) {
            return feature;
        })
        if (feature) {
          const clusterSize = feature.get('features').length;
          if (clusterSize > 1) {
            const extent = createEmpty();
            feature.get('features').forEach(function(feature) {
              extend(extent, feature.getGeometry().getExtent());
            });
            const options = {
              size: map.getSize(),
              padding: [paddingTop, paddingLeft, paddingBottom, paddingRight],
              duration: durationMilliseconds
            }
            map.getView().fit(extent, options);
          }
        }
      });
    },
  };
};

let wmsLayer = function(
  // layerName,
  // wmsLayerPath
) {
  /*
  This function allow to visualize WMS service on the map.
  layerName: string. It is the name that you choose for the WMS resource.
  wmsLayerPath: string. It is the url of WMS source.
  */
  // this.layerName = layerName;
  // this.wmsLayerPath = wmsLayerPath;

  let wms;

  return {
    'createWMSLayer': function(
      layerName,
      wmsLayerPath,
      wmslayerName,
      wmsLayerStyle,
      setMaxZoom,
      setMinZoom,
      setZIndex,
      setOpacity
    ) {
      /*
      This function create the WMS layer.
      wmslayerName: string. It is the name of the WMS resource
      wmsLayerStyle: string. It is the style of the WMS resource
      setMaxZoom: decimal. It's the max zoom level with which is possible to see the resource.
      setMinZoom decimal. It's the min zoom level with which is possible to see the resource.
      setZIndex: integer. It's the the level priority for the resource. The higher it is, the higher the position
                of the resource in the stack of layers.
      setOpacity: decimal. It is the opacity of the WMS resource, it'
                between 0.0 and 1.0.
      */
      this.wmslayerName = wmslayerName;
      this.wmsLayerStyle = wmsLayerStyle;
      this.setMaxZoom = setMaxZoom;
      this.setMinZoom = setMinZoom;
      this.setZIndex = setZIndex;
      this.setOpacity = setOpacity;

      wms = new ol.layer.Tile({
        title: layerName,
        source: new ol.source.TileWMS({
          url: wmsLayerPath,
          params: {
            'LAYERS': wmslayerName,
            'STYLES': wmsLayerStyle,
          }
        }),
        minZoom: setMinZoom,
        maxZoom: setMaxZoom,
        zIndex: setZIndex,
        opacity: setOpacity
      });
      // console.log(wms.getSource());

      return wms;
    },
  }

};

let wfsLayer = function(
  vectorType,
  layerName
){
  /*
  This function allow to visualize WFS service on the map.
  vectorType: string. It can be point, linestring and polygon.
  layerName: string. It is the name that you choose for the WFS resource.
  */
  this.vectorType = vectorType;
  this.layerName = layerName;

  let wfs;
  return {

    'createWFSLayer': function(
      wfsLayerPath,
      wfslayerName,
      setStrokeColor,
      setStrokeLineDashLength,
      setStrokeLineDashSpace,
      setStrokeWidth,
      setFillColor,
      setMaxZoom,
      setMinZoom,
      setZIndex
    ){
      /*
      This function create the WFS layer.
      wfsLayerPath: string. It is the url of WFS resource.
      wfslayerName: string. It is the name of the WFS resource
      setStrokeColor: string. It's the rgba color.
      setStrokeLineDashLength: decimal. It's a number that define the length of the dash. It's can be null.
      setStrokeLineDashSpace: decimal. It's a number that define the space between the dashes. It's can be null.
      setStrokeWidth: integer. This number define the stroke line's width.
      setFillColor: string. It's the rgba color.
      setMaxZoom: decimal. It's the max zoom level with which is possible to see the vector.
      setMinZoom decimal. It's the min zoom level with which is possible to see the vector.
      setZIndex: integer. It's the the level priority for the vector. The higher it is, the higher the position
                of the vector in the stack of layers.
      */
      this.wfsLayerPath = wfsLayerPath;
      this.wfslayerName = wfslayerName;
      this.setStrokeColor = setStrokeColor;
      this.setStrokeLineDashLength = setStrokeLineDashLength;
      this.setStrokeLineDashSpace = setStrokeLineDashSpace;
      this.setStrokeWidth = setStrokeWidth;
      this.setFillColor = setFillColor;
      this.setMaxZoom = setMaxZoom;
      this.setMinZoom = setMinZoom;
      this.setZIndex = setZIndex;

      let stroke, fill;
      stroke = new ol.style.Stroke({
          color: setStrokeColor,
          width: setStrokeWidth,
          lineDash: [setStrokeLineDashLength, setStrokeLineDashSpace],
          lineCap: 'butt',
          lineJoin: 'miter'
      });
      fill = new ol.style.Fill({
        color: setFillColor,
      });

      let style;
      // Change style based on the geometry type.
      if (vectorType.toLowerCase() === 'polygon') {
        style = new ol.style.Style({
            stroke: stroke,
            fill: fill
        });
      } else if (vectorType.toLowerCase() === 'linestring') {
        style = new ol.style.Style({
            stroke: stroke
        });
      } else if (vectorType.toLowerCase() === 'point') {
        style = new ol.style.Style({
            image: new ol.style.Circle({
              radius: setStrokeWidth * 5,
              stroke: stroke,
              fill: fill
            })
        });
      } else {
        console.error('Geometry not recognized! Accepted geometries: point, linestring, polygon.');
      }
      // Build the vector
      wfs = new ol.layer.Vector({
        title: layerName,
        source: new ol.source.Vector(),
        style: style,
        minZoom: setMinZoom,
        maxZoom: setMaxZoom,
        zIndex: setZIndex
      });
      /// Send features to WFS Source
      const wfsFeatureRequest = new ol.format.WFS().writeGetFeature({
        srsName: 'EPSG:3857',
        featureTypes: [wfslayerName],
        outputFormat: 'application/json',
      });
      async function getFeatureProperties() {
        let settings = {
          method: 'POST',
          body: new XMLSerializer().serializeToString(wfsFeatureRequest),
        }
        try {
          let response = await fetch(wfsLayerPath, settings);
          if (!response.ok) {
            throw new Error(`HTTP error!\n Status: ${response.status}\n Type: ${response.type}\n URL: ${response.url}`);
          } else {
            let data = await response.text();
            let json = JSON.parse(data);
            const features = new ol.format.GeoJSON().readFeatures(json);
            wfs.getSource().addFeatures(features);
          }
        } catch (e) {
          console.log(e);
        }
      }
      getFeatureProperties();

      return wfs;
    },
    'zoomToExtent': function(
      paddingTop,
      paddingLeft,
      paddingBottom,
      paddingRight,
      durationMilliseconds
    ){
      /*
      This function allow to zoom on the target vector's extent.
      paddingTop: integer. It is the top padding.
      paddingLeft: integer. It is the left padding.
      paddingBottom: integer. It is the bottom padding.
      paddingRight: integer. It is the right padding.
      durationMilliseconds: integer. Corresponds to how long the zoom lasts.
      */
      this.paddingTop = paddingTop;
      this.paddingLeft = paddingLeft;
      this.paddingBottom = paddingBottom;
      this.paddingRight = paddingRight;
      this.durationMilliseconds = durationMilliseconds;

      wfs.getSource().once('change', function(evt) {
        if (wfs.getSource().getState() === 'ready') {
          if (wfs.getSource().getFeatures().length > 0) {
            const extent = wfs.getSource().getExtent();
            const options = {
              size: map.getSize(),
              padding: [paddingTop, paddingLeft, paddingBottom, paddingRight],
              duration: durationMilliseconds
            }
            map.getView().fit(extent, options);
          }
        }
      });
    },
    'zoomOnLayer': function(
      paddingTop,
      paddingLeft,
      paddingBottom,
      paddingRight,
      durationMilliseconds
    ){
      /*
      This function activates the zoom by clicking on the button.
      paddingTop: integer. It is the top padding.
      paddingLeft: integer. It is the left padding.
      paddingBottom: integer. It is the bottom padding.
      paddingRight: integer. It is the right padding.
      durationMilliseconds: integer. Corresponds to how long the zoom lasts.
      */
      this.paddingTop = paddingTop;
      this.paddingLeft = paddingLeft;
      this.paddingBottom = paddingBottom;
      this.paddingRight = paddingRight;
      this.durationMilliseconds = durationMilliseconds;

      const extent = wfs.getSource().getExtent();
      const options = {
        size: map.getSize(),
        padding: [paddingTop, paddingLeft, paddingBottom, paddingRight],
        duration: durationMilliseconds
      }
      map.getView().fit(extent, options);
    },

  }
};
