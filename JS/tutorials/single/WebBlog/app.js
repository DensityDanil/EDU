const http = require('http');


http.createServer((request,response) => {
    console.log('hello from Ukraine');
    response.end('You know that this is just text and white background');
}).listen(3000)