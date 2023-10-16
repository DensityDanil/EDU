var number=function(array){
    var out = [];
    for(var i=0;i<array.length;i++){
      
      var pair = array[i] +': '+ i.toString();
      //console.log(pair);
      out.push(pair);  
  }

  }

number(['a','b','c']);