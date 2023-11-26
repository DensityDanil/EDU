
try{
    Promise.resolve(1).then((x) => 
    {throw new Error("err");
    });
} catch (e) {
    console.log("error");
}
