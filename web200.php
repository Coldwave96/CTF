<?php
function decode($str){
    $s = base64_decode(strrev((str_rot13($str))));

    $res='';
    for($i=0; $i<strlen($s); $i++){
        $tmp = substr($s, $i, 1);
        $__ = chr(ord($tmp)-1);
        $res = $res.$__;
    }
    $flag = strrev($res);
    return $flag;
}

    echo decode('a1zLbgQsCESEIqRLwuQAyMwLyq2L5VwBxqGA3RQAyumZ0tmMvSGM2ZwB4tws');
?>
