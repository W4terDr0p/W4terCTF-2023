const express = require("express")
const fs = require("fs")
const cookieParser = require("cookie-parser");
const controller = require("./controller")

const app = express();
const PORT = Number(process.env.PORT) || 80
const HOST = '0.0.0.0'


app.use(express.urlencoded({ extended: false }))
app.use(cookieParser())
app.use(express.json())

app.use(express.static('static'))

app.get("/", (res) => {
    res.sendFile(__dirname, "static/index.html")
})

app.post("/", (req, res) => {
    controller.LoginController(req, res)
})

app.get("/flag1", (req, res) => {
    controller.Flag1Controller(req, res)
})

app.post("/flag2", (req, res) => {
    controller.Flag2Controller(req, res)
})

app.listen(PORT, HOST, () => {
    console.log(`Server is listening on Host ${HOST} Port ${PORT}.`)
})
