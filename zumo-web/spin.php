<?php
$angle=$_GET['angle'];
$t=abs($angle*5555);
system("pigs w 23 0");
system("pigs w 22 0");
system("pigs w 24 0");
system("pigs w 27 0");
if ($angle>0){
system("pigs w 23 1");
system("pigs w 22 1");
usleep($t);
system("pigs w 23 0");
system("pigs w 22 0");
}else if ($angle<0){
system("pigs w 24 1");
system("pigs w 27 1");
usleep($t);
system("pigs w 24 0");
system("pigs w 27 0");
}
?>
