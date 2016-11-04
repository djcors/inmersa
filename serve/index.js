var express = require('express')
var serveStatic = require('serve-static')

var app = express()

app.use(serveStatic('../inmersa', {'index': ['home.html', ]}))
app.listen(3000)
