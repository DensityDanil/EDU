var reduce = function(nums, fn, init) {
    var out = init;
    if(nums.length>0)
    {
    out = 0;
    for(var i=0;i<nums.length;i++){
        var elem = nums[i]+init;
        var modified_elem = fn(out,elem) ;
        if (modified_elem){
            console.log(out);
            out+=modified_elem;
            };
    }
}
    return out;
};

var test1 = [[1,2,3,4],function sum(accum, curr) { return accum + curr; },0];

var idx = 0;
var t1 = test1[idx][0];
var t2 = test1[idx][1];
var t3 = test1[idx][2];


var r1 = reduce(t1,t2,t3);
console.log(r1)