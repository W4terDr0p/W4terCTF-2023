<?php
    highlight_file(__FILE__);
    // something in flag.php

    class A
    {
        public $a;
        public $b;

        public function __wakeup()
        {
            $this->a = "hacker?";
        }

        public function __invoke()
        {
            if (isset($this->a) && $this->a == md5($this->a)) {
                $this->b->uwant();
            }
        }
    }

    class B
    {
        public $a;
        public $b;
        public $k;

        function __destruct()
        {
            $this->b = $this->k;
            die($this->a);
        }
    }

    class C
    {
        public $a;
        public $c;

        public function __toString()
        {
            $cc = $this->c;
            return $cc();
        }
        public function uwant()
        {
            if ($this->a == "phpinfo") {
                phpinfo();
            } else {
                $this->a->unexist_function();
            }
        }
    }

    if(isset($_GET["data"])){
        unserialize($_GET["data"]);
    }
?>
