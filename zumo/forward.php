<?php
if(isset($_GET['time'])){
  $useconds=abs($_GET['time'])/1000000.0;
}else{
  $useconds=1000000;
}  
system("pigs w 23 1");
system("pigs w 27 1");
system("pigs w 24 0");
system("pigs w 22 0");
usleep($useconds);
system("pigs w 23 0");
system("pigs w 27 0");
?>
