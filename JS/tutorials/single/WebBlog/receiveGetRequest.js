
//before https://youtu.be/YMJDUHUccvA?t=659
const http = require('http');
const url = require('url');


http.createServer((request,response) => {
    console.log('Hola from Ukraine server');
    //console.log(request.method)
    let urlRequest = url.parse(request.url,true);
    console.log(urlRequest.query.test);
    if 

//     if (request.method=='GET'){
//         if(urlRequest.query.test==='300')
//         {
        
//         //console.log(500);
//         console.log(500);
//         response.end('You know that this is just text and white background');
//         }

// }
}).listen(3000)