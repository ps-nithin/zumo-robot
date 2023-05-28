<?php
$link=$_GET['ytlink'];
echo $link;
system("yt-dlp -g --format bestaudio $link | cvlc - vlc://quit");
?>
