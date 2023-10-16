function solution(str){
  var l = str.length; 
  var arr = [];
  
  if (l%2==1){
    str = str+'_';
  }
  
  for(var i=0;i<l;i=i+2){  
    var val = str.slice(i,i+2);
    arr.push(val);}
  
  return arr;
  
}