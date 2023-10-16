

var argumentsLength = function(...args) {
    var out = 0;
    for(var i=0;i<args.length;i++){
        out += 1
    }
    return out;
};

var r1 = argumentsLength(1, 2, 3);
console.log(r1);

