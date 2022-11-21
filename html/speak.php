<?php
$text_to_speak=$_POST['text'];
system("espeak-ng -vmb-en1 -s200 -p75 -g15 '$text_to_speak'");
?>
