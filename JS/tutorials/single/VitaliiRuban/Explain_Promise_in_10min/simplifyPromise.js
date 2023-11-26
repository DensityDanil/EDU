(async function() {
    var res = await Promise.resolve(1);
    res++;
    console.log(res);
})();