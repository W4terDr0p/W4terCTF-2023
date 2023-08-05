<?php
    highlight_file(__FILE__);
    if($_SERVER["REMOTE_ADDR"] === "127.0.0.1") {
        system("cat /flag >> flag.txt");
    }
?>
