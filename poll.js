// setInterval to request /textRefresher
// embed this javascript into the indext.html

// looks kind of like, which is a callback
//a callback is for the asynchronicity of querying the server
// $.ajax(location/textRefresher, function(newText){put into div})

//timing stuff setTimeout, based on comparing previous string to current newtext


$(function worker() {
	console.log("app started")
  $.ajax({
  	//below means the relative location and then the specified route
    url: window.location.href+'/textRefresher', 
    success: function(textRefresher) {
    	console.log(textRefresher);
    	//$('#text')
      //here is where we need to pass the return from python and append to div
    },
    complete: function() {
      // Schedule the next request when the current one's complete
      setTimeout(worker, 1000);
    }
  });
});