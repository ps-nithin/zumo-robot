<?php
$voice=$_FILES['audio_data']['tmp_name'];
system("cvlc $voice");
?>
