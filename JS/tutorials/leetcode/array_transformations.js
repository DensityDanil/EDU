var map = function(arr, fn) {
    var out = [];
    for(var i=0;i<arr.length;i++){
        var elem = fn(arr[i],i);
        out.push(elem);
}
    return out;
};

// Передаємо функцію fn як аргумент
var tests = [[function plusI(n, i) { return n + i; },[1,2,3]]];

// Викликаємо функцію map
var r = map(tests[0][1],tests[0][0]);
console.log(r);
