
//before https://youtu.be/YMJDUHUccvA?t=659
const http = require('http');
const http = require('url');


http.createServer((request,response) => {
    console.log('hello from Ukraine server');
    console.log(request.method);
    let urlRequest = url.parse(request.url,true);
    console.log(urlRequest);
    response.end('You know that this is just text and white background');
}).listen(3000)