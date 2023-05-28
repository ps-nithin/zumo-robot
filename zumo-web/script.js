let recorder,audio_stream;
const preview=document.getElementById("audio-playback");
const downloadAudio=document.getElementById("downloadButton");
const snapshot=document.getElementById("snapshot");
var mjpeg_img;

$(document).ready(function(){
  setTimeout('init();',100);
  $('#stopButton').attr("disabled",true);
  $('#forward').click(function(){
    this_=$(this);
    var s=$('#dutycycle').val();
    this_.css("background-color","lightblue");
    $.get("forward.php",{dutycycle: s},function(data,status_){
      updateImage(this_);
    });
  });
  $('#backward').click(function(){
    this_=$(this);
    var s=$('#dutycycle').val();
    this_.css("background-color","lightblue");
    $.get("backward.php",{dutycycle:s},function(data,status_){
      updateImage(this_);
    });
  });
  $('#rotateButton').click(function(){
    this_=$(this);
    this_.css("background-color","lightblue");
    var s=$('#dutycycle').val();
    var a=$('#angle').val();
    $.get("spin.php",
	    {angle:a,dutycycle:s},
	    function(data,status_){
            updateImage(this_);
    });
  });

  $('#spin_cw').click(function(){
    this_=$(this);
    this_.css("background-color","lightblue");
    $.get("spin.php",{angle:-15,dutycycle:255},function(data,status_){
      updateImage(this_);
    });
  });
  $('#spin_acw').click(function(){
    this_=$(this);
    this_.css("background-color","lightblue");
    $.get("spin.php",{angle:15,dutycycle:255},function(data,status_){
      updateImage(this_);
    });
  });
  $('#stop').click(function(){
    this_=$(this);
    this_.css("background-color","lightblue");
    $.get("stop.php",function(data,status_){
	$('.menu_item_motor').css("background-color","white");
    });
  });

  $('#speak').click(function(){
    text_to_speak=$('#text_to_speak').val();
    if (text_to_speak.length==0){
      return 0;
    }
    this_=$(this);
    this_.prop("disabled",true);
    this_.html("Playing ...");
    $.post("speak.php",{text: text_to_speak},function(status_){
      this_.prop("disabled",false);
      this_.html("Speak!");
    });
  });

  $('#recordButton').click(function(){
    $(this).css("background-color","lightblue");
    startRecording();
    $('#stopButton').attr("disabled",false);
  });
  $('#stopButton').click(function(){
    $('#recordButton').css("background-color","white");
    stopRecording();
  });
  $('#downloadButton').click(function(){
    this_=$(this);
    downloadRecording(this_);
  });
  $('#updateSnapshot').click(function(){ 
    $(this).css("background-color","lightblue");
    updateImage($(this));
  });

  $('#playMusic').click(function(){
    var url=$('#yt_link').val();
    if (url.length==0){
      return 0;
    }
    this_=$(this);
    $('#playMusic').prop("disabled",true);
    this_.html("Playing ...");
    $.get('play_music.php',{ytlink:url},function(data,status_){
      this_.prop("disabled",false);
      this_.html("Play!");
    });
  });
  $('#stopMusic').click(function(){
    $.get('stop_music.php',function(data,status_){
      $('#playMusic').prop("disabled",false);
      $('#playMusic').html("Play!");
    });
  });

});

function reload_img(){
  mjpeg_img.src="cam_pic.php?time="+new Date().getTime();
}

function error_img(){
  setTimeout("mjpeg_img.src='cam_pic.php?time='+new Date().getTime();",100);
}

function init(){
  mjpeg_img=document.getElementById("mjpeg_dest");
  mjpeg_img.onload=reload_img;
  mjpeg_img.onerror=error_img;
  reload_img();
}

function updateImage(this_){
  /*
  $.get({
    url: "get_image.php",
    cache: false,
    async: true
  }).then(function (data,status_){
    snapshot.src="second.jpg?t="+Math.random();
    this_.css("background-color","white");
  });
  */
  this_.css("background-color","white");
}

recordedChunks=[];
blobLink=0;
voiceBlob=0;
function startRecording(){
  navigator.mediaDevices.getUserMedia({audio:true})
    .then(function(stream){
      audio_stream=stream;
      recorder=new MediaRecorder(stream);
      recorder.ondataavailable=function(e){
        const url=URL.createObjectURL(e.data);
	if (e.data.size>0) recordedChunks.push(e.data);
	preview.src=url;
	downloadAudio.href=url;
      };
      recorder.addEventListener('stop',function(){
	voiceBlob=new Blob(recordedChunks);
        blobLink=URL.createObjectURL(new Blob(recordedChunks));
      });
      recorder.start();
      timeout_status=setTimeout(function(){
        console.log("5 min timeout");
	stopRecording();
      },300000);
    });
}

function stopRecording(){
  recorder.stop();
  audio_stream.getAudioTracks()[0].stop();
}

function downloadRecording(this_){
  var name=new Date();
  var res=name.toISOString().slice(0,10);
  var fileName=res+'.wav';
  var fd=new FormData();
  fd.append("audio_data",voiceBlob,fileName);
  this_.html("Playing ...");
  this_.prop("disabled",true);
  $.ajax({
    url: "voice.php",
    method: "POST",
    processData: false,
    contentType: false,
    data: fd,
    enctype: 'multipart/form-data',
    success: function(data){
	this_.prop("disabled",false);
	this_.html("Send audio!");
    },
    error: function(err){
      ;
    }
  });
  //location.reload();
}
