//var map = L.map('map').setView([46.168429, 9.874529], 9);
var jsonLayer = null;

        function provando(direction){
            var prova = document.getElementById("prova");
            if(direction == 'next')
                prova.value=parseInt(prova.value)+1
            else
                prova.value=parseInt(prova.value)-1
            return prova.value
        }
        //var map = L.map('map').setView([46.168429, 9.874529], 9);

function changeState(direction){
    state = provando(direction)

    d3.json("states/?state="+state).then(function(e){
    
    console.log(e["event_description"])
    console.log(e["data"])

    a = e["event_description"];
    // update description on the intended div
    var event_display = document.getElementById("event");
    event_display.textContent = a
    e = e["data"]

    console.log(e)
    var popupContent = "";
    var currentHover = null;    
    var hovermarker = null;
    var areas;
    var topoj;

    function dashedFeature(feature,layer) {                
        layer.setStyle({
            className: 'territory '+feature.properties.comune,   
            //dashArray: '5, 10',
            color: "black",
            fillColor: feature.properties.color,
            fillOpacity: 1,
            weight: 1
        })
        popupContent = "<p>"+feature.properties.comune+" controllato da "+feature.properties.owner;		
        layer.bindPopup(popupContent);
    }

    function lableFeature(feature,layer) {
        layer.setStyle({
            dashArray: null,
            color: null,
            fillColor: null,
            fillOpacity: 0,
        })
        // FORSE, NON SONO MOLTO BELLE E OCCUPANO UN BEL PO' DI SPAZIO
        var label = L.marker(layer.getBounds().getCenter(), {
        icon: L.divIcon({
            className: 'label',
            //devo modificare lo zoom a runtime con map.on("zoomend", function(){ ... })
            html: "<p style='font-size:"+1000/map.getZoom()+"%;' >"+feature.properties.comune+"</p>"
            //iconSize: [100, 40]
        })
        }).addTo(map);
    }
    
    function countryFeature(feature,layer) {
        layer.setStyle({
            className: 'country-'+feature.properties.ADMIN,
            fillColor: countries.get(feature.properties.ADMIN).color,
            fillOpacity: 1,                         
            color: "black",
            weight: 1
        })
    }

    function countryHover(feature,layer) {
        layer.setStyle({            
            fill: false,                      
            color: "limegreen",
            weight: 3
        })
    }

    function showHover(newHover){        
        true;
    }

    // STA ROBA FA UN PO' CAGARE
    // map.on("zoomend", function() {
    //     if(map.hasLayer(lableLayer)){
    //         map.removeLayer(lableLayer)
    //     }
    //     var lableLayer = L.geoJSON(e, {onEachFeature: lableFeature}).addTo(map)
    // });

    if(map.hasLayer(jsonLayer)){
        map.removeLayer(jsonLayer)
    }

    jsonLayer = L.geoJSON(e, {onEachFeature: dashedFeature}).addTo(map);       
    jsonLayer.on("touchmove", function (event) {              
        showHover(event.layer.feature.properties.owner);
    });
    jsonLayer.on("mousemove", function (event) {                  
        showHover(event.layer.feature.properties.owner);
    });
    jsonLayer.on("click", function (event) {   
        console.log(event)               
    });
    jsonLayer.addTo(map);
    });

}