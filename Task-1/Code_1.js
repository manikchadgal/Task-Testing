// buggy_server.js
const express = require("express");

const app = express;

app.get("/", (req, res) => {
    res.send("Hello, FOSS!")
}

app.listen(3000)
console.log("Server running at http://localhost:3000");
