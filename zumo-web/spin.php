<?php
$UPTIME_MOTORS="/home/pi/uptime_motors.txt";
if(isset($_GET['angle'])){
  $angle=$_GET['angle'];
}else{
  $angle=40;
}  
if(isset($_GET['dutycycle']) && !empty($_GET['dutycycle'])){
  $dutycycle=$_GET['dutycycle'];
}else{
  $dutycycle=75;
}
system("pigs pfs 23 100 pfs 22 100 pfs 24 100 pfs 27 100");
$t=abs($angle*5555);
system("pigs p 23 0 p 22 0 p 24 0 p 27 0");
if ($angle>0){
system("pigs p 23 $dutycycle p 22 $dutycycle");
usleep($t);
system("pigs p 23 0 p 22 0");
}else if ($angle<0){
system("pigs p 24 $dutycycle p 27 $dutycycle");
usleep($t);
system("pigs p 24 0 p 27 0");
}
$utfile=fopen($UPTIME_MOTORS,'r');
$ut_pre=fread($utfile,filesize($UPTIME_MOTORS));
fclose($utfile);
$utfile=fopen($UPTIME_MOTORS,'w');
fwrite($utfile,$ut_pre+$t/1000000);
fclose($utfile);
?>
