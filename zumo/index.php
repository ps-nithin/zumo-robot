<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>zumo robot</title>
<script src="jquery-3.6.1.min.js"></script>

<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<!--<img id="streamImage" src="http://192.168.1.25:8080/?action=stream"/><br>
-->
<div id="snapshotDiv"><img id="snapshot" src="second.jpg" class="menu_item"></img></div><hr>
<button type="button" id="backward" class="menu_item">Backward</button>
<button type="button" id="forward" class="menu_item">Forward</button><br>
<button type="button" id="spin_cw" class="menu_item">Left</button>
<button type="button" id="spin_acw" class="menu_item">Right</button><br>
<button type="button" id="rotateButton" class="menu_item">Rotate</button>
<input id="angle" class="menu_item" type="number" min="-180" max="180" placeholder="Angle ..."/><br>
<button type="button" id="stop" class="menu_item">Stop</button>
<button type="button" id="updateSnapshot" class="menu_item">Update image</button><hr>
<textarea id="text_to_speak" placeholder="Say something ..." class="menu_item"></textarea><br>
<button type="button" id="speak" class="menu_item">Speak!</button><hr>
<div class="audio-record">
<div class="playback">
<audio src="" controls id="audio-playback"></audio>
</div>
<button id="recordButton" class="menu_item">Start Recording</button>
<button id="stopButton" class="menu_item">Stop</button></div>
<button id="downloadButton" class="menu_item">Send Audio</button><hr>
<input id="yt_link" class="menu_item" placeholder="Youtube link ..."/>
<button id="playMusic" class="menu_item">Play</button>
<button id="stopMusic" class="menu_item">Stop</button><p>
<script src="script.js"></script>
</body>
</html>
