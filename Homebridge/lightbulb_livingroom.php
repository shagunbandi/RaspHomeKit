<?php

include_once "/lib/sd_340.php";

define("OUT_PIN", 2);

uio_setup(2, OUT_PIN, "out");

if(($led0 = _GET("On")))
{
	if($led0 ===  "true")
		uio_out(2, OUT_PIN, LOW);
	else
		uio_out(2, OUT_PIN, HIGH);
}

if(uio_in(2, OUT_PIN) == LOW)
	echo '{"On" : true}';
else
	echo '{"On" : false}';

?>