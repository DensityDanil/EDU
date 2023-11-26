async function f1(num) {
    var res = await Promise.resolve(num);
    res++;
    //console.log(res);
    return res;
};


async function f2(num) {
    var start = await f1(num);
    var res = await Promise.resolve(start);
    res++;
    console.log(res);
};

f2(1);