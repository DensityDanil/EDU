function testCycle(n) {

  let x = [];
  for(var i=1;i<=n;i++){
      if(i!==1)
      {
          let formula_calc = 2 * x[1] - 1;
          x.push(formula_calc);
      }
      else{
          let formula_calc = 2 * x[i] -1;
          x.push(formula_calc);
      }
  }

  return x.join(' ');
}

let n = Number(prompt())
console.log(testCycle(n))