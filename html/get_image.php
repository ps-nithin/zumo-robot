<?php
system("raspistill -w 320 -h 320 -rot 180 -o first.jpg");
$c1='convert -pointsize 10 -fill yellow -draw "text 90,310 ';
$date=system("date");
$c2='\'Last updated on '.$date.'\'';
$c3='" first.jpg second.jpg';
system($c1.$c2.$c3);
?>
