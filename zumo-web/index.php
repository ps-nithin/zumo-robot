<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>zumo robot</title>
<script src="jquery-3.6.1.min.js"></script>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div class="header_wrap">
<div class="header_div">
<div class="menu_item act_menu first_menu_item"><a href="index.php">Home</a>
</div>
</div></div>
<div class="content_div">
<!--
<div id="snapshotDiv"><img id="snapshot" src="second.jpg" class="menu_item"></img></div><hr>
-->
<div class="container"><img id="mjpeg_dest" class=""></img></div>
<div class="wrapper">
<div class="container"><h1>Move the robot</h1><hr>
<button type="button" id="backward" class="menu_item_motor">Backward</button>
<button type="button" id="forward" class="menu_item_motor">Forward</button><br>
<button type="button" id="spin_cw" class="menu_item_motor">Left</button>
<button type="button" id="spin_acw" class="menu_item_motor">Right</button><br>
<button type="button" id="rotateButton" class="menu_item_motor">Rotate</button>
<input id="angle" class="menu_item_motor" type="number" min="-180" max="180" placeholder="Angle ..."/><input id="dutycycle" class="menu_item_motor" type="number" min="0" max="255" placeholder="Speed : 0-255"/><br>
<button type="button" id="stop" class="menu_item_motor">Stop</button>
<!--
<button type="button" id="updateSnapshot" class="menu_item">Update image</button>-->
</div><div class="container"><h1>Text to speech</h1><hr>
<textarea id="text_to_speak" placeholder="Say something ..." class="menu_item"></textarea><br>
<button type="button" id="speak" class="menu_item">Speak!</button></div>
<div class="container">
<h1>Speak live</h1><hr>
<div class="audio-record">
<div class="playback">
<audio src="" controls id="audio-playback"></audio>
</div>
<button id="recordButton" class="menu_item">Start Recording</button>
<button id="stopButton" class="menu_item">Stop</button></div>
<button id="downloadButton" class="menu_item">Send Audio!</button>
</div><div class="container"><h1>Play Youtube audio</h1><hr>
<input id="yt_link" class="menu_item" placeholder="Youtube link ..."/>
<button id="playMusic" class="menu_item">Play!</button>
<button id="stopMusic" class="menu_item">Stop</button><p></div>
<script src="script.js"></script>
</div></div>
</body>
</html>
