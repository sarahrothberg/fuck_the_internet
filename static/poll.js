// setInterval to request /textRefresher
// embed this javascript into the indext.html

// looks kind of like, which is a callback
//a callback is for the asynchronicity of querying the server
// $.ajax(location/textRefresher, function(newText){put into div})

//timing stuff setTimeout, based on comparing previous string to current newtext

var currentText;
var lastText;
var isQuestion; 

$(function(){
  mainFunction();
  isQuestion = window.location.hash==="#Qs"; 

});
//when jquery say that the DOM is ready, it calls this function, 

function mainFunction(){
  worker();
  // valerie();
  setTimeout(mainFunction, 10000);
}
//the above is like a drawloop

//mainFunction();
//this is not processing. you can call a function whenever, as long as its been defined

function hasChanged(){
  if (!isQuestion){
    console.log("this si the anwer machine")
  } else {
    console.log("this si the question machine")
  }


  console.log("changed!")
  processing();
}

function worker(){
  $.ajax({
      //below means the relative location and then the specified route
      url: location.protocol+'//'+location.host+location.pathname+'textRefresher', 
      success: function(textMessage) {
        $('#text').html(textMessage);
        currentText = textMessage;
        if (currentText != lastText){
          hasChanged();
          lastText = currentText;
        }
      },
    });
}

          // MACK'S STUFF GIPHY QUERY
function macksThing(){
  var xhr = $.get("http://api.giphy.com/v1/gifs/search?q=" + lastText +"&api_key=dc6zaTOxFJmzC&limit=5");
  xhr.done(function(data) {
    var embedURL = data['data'][0].images.original.url;
    var img = new Image(); 
    $('#gifAnswer').html(img); 
    img.src = embedURL; 
  });
}

function processing(){
  $('#isProcessing').addClass('processing');

  if (isQuestion){
      setTimeout(questionAppear, 5000);
  }
  else {
      setTimeout(answerAppear, 5000)
  }
}

function questionAppear(){
  $('#isProcessing').removeClass('processing'); 

}

function answerAppear(){
  $('#isProcessing').removeClass('processing');
  macksThing();
}

// function valerie(){
//           $.ajax({
//             url: window.location.href+'sendSerial',
//             type: 'GET',                
//                 success: function(data) {
//                   console.log('triggering serial')
//                   //HERE IS THE PROBLEM - how to call the /sendSerial route? 
//                   window.location.href+'sendSerial'.reload(true);  
//                   // window.location.href+'sendSerial' = window.location.href+'sendSerial'; 
//                 }
//           });
//   });
// }