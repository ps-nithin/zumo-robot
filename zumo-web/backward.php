<?php
if (isset($_GET['time'])){
  $useconds=abs($_GET['time'])*1000000.0;
} else {
  $useconds=1000000;
}
if(isset($_GET['dutycycle']) && !empty($_GET['dutycycle'])){
  $dutycycle=$_GET['dutycycle'];
}else{
  $dutycycle=255;
}
system("pigs pfs 24 100 pfs 22 100");
system("pigs p 24 $dutycycle p 22 $dutycycle");
usleep($useconds);
system("pigs p 24 0 p 22 0");
$UPTIME_MOTORS="/home/pi/uptime_motors.txt";
$utfile=fopen($UPTIME_MOTORS,'r');
$ut_pre=fread($utfile,filesize($UPTIME_MOTORS));
fclose($utfile);
$utfile=fopen($UPTIME_MOTORS,'w');
fwrite($utfile,$ut_pre+$useconds/1000000);
fclose($utfile);
?>
