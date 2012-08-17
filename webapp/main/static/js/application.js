var map;
var marknum = 0;
var geocoder;
var center_marker;

function initialize() {
  var myLatlng = null;
  if(marks.length>0) {
    var lastmark = marks[marks.length-1];
    myLatlng = new google.maps.LatLng(lastmark['fields']['lat'], lastmark['fields']['lon']);
  } else {
    myLatlng = new google.maps.LatLng(37.751, -122.433);
  }
  var mapOptions = {
    zoom: 13,
    center: myLatlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  // creates the map 
  map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
  // creates new mark on map
  google.maps.event.addListener(map, 'click', function(event) {
  // passing in the latlng into the show_postbox function 
    show_postbox(event.latLng);
  });
  console.log(marks);
  // updates map with all marks in database/json object 
  for (i=0; i<marks.length; i++) {
    mark_latlng = new google.maps.LatLng(marks[i]['fields']['lat'], marks[i]['fields']['lon']);
    console.log(mark_latlng);
    placeMarker(mark_latlng, marks[i]['pk']);
  }

  center_marker = new google.maps.Marker({
    position: myLatlng,
    map: map,
    draggable: false
  });

  geocoder = new google.maps.Geocoder();
}

// new markers
function placeMarker(location,pk) {
  var marker = new google.maps.Marker({
    position: location,
    map: map,
    draggable: true,
    // user icon, need to make it per user 
    icon: "/static/img/meeh.jpg"
  });
  google.maps.event.addListener(marker, 'click', function() {
      show_lightbox(pk);
  });
}


// matches pk of mark against the json 
function lookup_mark(pk) {
  for(var i=0;i<marks.length;i++) {
    if (marks[i]['pk'] == pk) {
      return marks[i];
    }
  }
  return false;
  // don't refresh 
}

// puts json into the lightbox
function show_lightbox(pk) {
  var mark = lookup_mark(pk);
  var img_html = "";
  img_html += "<img src=\"";
  img_html += mark['fields']['img'];
  img_html += "\">";
  alert(img_html)
  $("div#lb_title").html(mark['fields']['title']);
  $("div#lb_body").html(mark['fields']['body']);
  $("div#lb_image").html(img_html);
  //$("div#lb_image").html(mark['fields']['img'])
  $("div#lightbox").show();
  marknum++;
  return false;
};


function hide_lightbox() {
  $("div#lightbox").hide();
  return false;
};


function show_postbox(latLng) {
  $("div#postnote").show();
  $("#lon").val(latLng.lng());
  $("#lat").val(latLng.lat());
  return false; 
};


function hide_postbox() {
  $("div#postnote").hide();
  return false; 
  // prevents page from refreshing 
};

function show_ticker() {
  var tick_html = "";
  for(var i=0;i<marks.length;i++) {
    tick_html += "<div>";
    tick_html += marks[i]['fields']['title'];
    tick_html += marks[i]['fields']['body'];
    tick_html += "</div>";
  }
  $("div#ticker").html(tick_html);
  $("div#ticker").show();
  return false; 
};

function hide_ticker() {
  $("div#ticker").hide();
  return false; 
};

// search bar           
function search() {
  $("#address").autocomplete ({
    // uses the geocoder to get address values
    source: function(request, response) {
      geocoder.geocode( {'address': request.term }, function(results, status) {
        response($.map(results, function(item) {
          return {
            label: item.formatted_address,
            value: item.formatted_address,
            latitude: item.geometry.location.lat(),
            longitude: item.geometry.location.lng()
          }
        }));
      })
    },
    // execute with selected address
    select: function(event, ui) {
      $("#latitude").val(ui.item.latitude);
      $("#longitude").val(ui.item.longitude);
      var location = new google.maps.LatLng(ui.item.latitude, ui.item.longitude);
      map.setCenter(location);
      center_marker.setPosition(location);
    }
  });
};

// same as html-body-onload 
$(document).ready(function(){
  $("a#xclose").click(hide_lightbox);
  $("a#closepost").click(hide_postbox);
  $("a#apostnote").click(show_postbox);
  $("a#ticker").click(show_ticker);
  $("a#xticker").click(hide_ticker);
  initialize();
  search();
});