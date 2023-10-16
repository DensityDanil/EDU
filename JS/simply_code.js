function squareDigits(num){
    var num_string = num.toString();
    var out_string = '';

    for(var i=0;i<num_string.length;i++){
      var num_transform = parseInt(num_string[i])**2;
      console.log(num_transform);
      out_string+=num_transform;

    }
    return out_string;
  }


var res = squareDigits(-3045);

