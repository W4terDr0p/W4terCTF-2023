const fs = require("fs");
const SECRET_COOKIE = process.env.SECRET_COOKIE || "this_is_testing_cookie"

const flag1 = fs.readFileSync("/flag1")
const flag2 = fs.readFileSync("/flag2")

function merge(target, source) {
    for (let key in source) {
        if (key == "__proto__") {
            continue; // no proto， please bypass
        }
        if (key in target && key in source) {
            merge(target[key], source[key])
        } else {
            target[key] = source[key]
        }
    }
}

function LoginController(req, res) {
    try {
        let user = {}
        merge(user, req.body)

        if (user.username !== "admin" || user.password !== Math.random().toString()) {
            res.status(401).type("text/html").send("Login Failed")
        } else {
            res.cookie("user", SECRET_COOKIE)
            req.user = "admin"
            res.redirect("/flag1")
        }
    } catch (e) {
        console.log(e)
        res.status(401).type("text/html").send("What the heck")
    }
}

function Flag1Controller(req, res) {
    try {
        if (req.cookies.user === SECRET_COOKIE || req.user == "admin") {
            res.setHeader("This_Is_The_Flag1", flag1.toString().trim())
            res.status(200).type("text/html").send("Login success. Welcome,admin!")
        } else {
            res.status(401).type("text/html").send("Unauthorized")
        }
    } catch (__) { }
}

function Flag2Controller(req, res) {
    let checkcode = req.body.checkcode ? req.body.checkcode : 1234;
    console.log(req.body)
    if (checkcode.length === 16) {
        try {
            checkcode = checkcode.toLowerCase()
            if (checkcode !== "aGr5AtSp55dRacer") {
                res.status(403).json({ "msg": "Invalid Checkcode1:" + checkcode })
            }
        } catch (__) { }
        res.status(200).type("text/html").json({ "msg": "You Got Another Part Of Flag: " + flag2.toString().trim() })
    } else {
        res.status(403).type("text/html").json({ "msg": "Invalid Checkcode2:" + checkcode })
    }
}

module.exports = {
    LoginController,
    Flag1Controller,
    Flag2Controller
}
