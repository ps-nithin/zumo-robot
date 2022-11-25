let recorder,audio_stream;
const preview=document.getElementById("audio-playback");
const downloadAudio=document.getElementById("downloadButton");
const snapshot=document.getElementById("snapshot");

$(document).ready(function(){

  $('#stopButton').attr("disabled",true);
  $('#forward').click(function(){
    this_=$(this);
    this_.css("background-color","lightblue");
    $.get("forward.php",function(data,status_){
      updateImage(this_);
    });
  });
  $('#backward').click(function(){
    this_=$(this);
    this_.css("background-color","lightblue");
    $.get("backward.php",function(data,status_){
      updateImage(this_);
    });
  });
  $('#rotateButton').click(function(){
    this_=$(this);
    this_.css("background-color","lightblue");
    var a=$('#angle').val();
    $.get("spin.php",
	    {angle: a},
	    function(data,status_){
            updateImage(this_);
    });
  });

  $('#spin_cw').click(function(){
    this_=$(this);
    this_.css("background-color","lightblue");
    $.get("spin.php",{angle:-10},function(data,status_){
      updateImage(this_);
    });
  });
  $('#spin_acw').click(function(){
    this_=$(this);
    this_.css("background-color","lightblue");
    $.get("spin.php",{angle:10},function(data,status_){
      updateImage(this_);
    });
  });
  $('#stop').click(function(){
    this_=$(this);
    this_.css("background-color","lightblue");
    $.get("stop.php",function(data,status_){
      this_.css("background-color","white");
    });
  });

  $('#speak').click(function(){
    text_to_speak=$('#text_to_speak').val();
    $.post("speak.php",{text: text_to_speak},function(status_){
      ;
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
    downloadRecording();
  });
  $('#updateSnapshot').click(function(){ 
    $(this).css("background-color","lightblue");
    updateImage($(this));
  });

  $('#playMusic').click(function(){
    var url=$('#yt_link').val();
    this_=$(this);
    $('#playMusic').css("background-color","lightblue");
    $('#playMusic').prop("disabled",true);
    $.get('play_music.php',{ytlink:url},function(data,status_){
      this_.css("background-color","white");
      this_.prop("disabled",false);
    });
  });
  $('#stopMusic').click(function(){
    $.get('stop_music.php',function(data,status_){
      $('#playMusic').prop("disabled",false);
    });
  });

});

function updateImage(this_){
  $.get({
    url: "get_image.php",
    cache: false,
    async: true
  }).then(function (data,status_){
    snapshot.src="second.jpg?t="+Math.random();
    this_.css("background-color","white");
  });
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

function downloadRecording(){
  var name=new Date();
  var res=name.toISOString().slice(0,10);
  var fileName=res+'.wav';
  var fd=new FormData();
  fd.append("audio_data",voiceBlob,fileName);
  $.ajax({
    url: "voice.php",
    method: "POST",
    processData: false,
    contentType: false,
    data: fd,
    enctype: 'multipart/form-data',
    success: function(data){
        alert(data);
    },
    error: function(err){
      ;
    }
  });
  location.reload();
}
