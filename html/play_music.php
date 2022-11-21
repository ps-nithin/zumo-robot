<?php
$link=$_GET['ytlink'];
echo $link;
system("youtube-dl -g --format bestaudio $link | cvlc - vlc://quit");
?>
