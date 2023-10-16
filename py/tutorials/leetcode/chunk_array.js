var chunk = function(arr, size) {
    var out = [];
    for(var i=0;i<arr.length;i = i+size){
        var arr_chunk = arr.slice(i,i+size);
        out.push(arr_chunk);
    }
    return out;  
};
