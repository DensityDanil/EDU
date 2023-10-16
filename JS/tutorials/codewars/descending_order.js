// Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
// Examples:
// Input: 42145 Output: 54421
// Input: 145263 Output: 654321
// Input: 123456789 Output: 987654321

//https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/javascript
function descendingOrder(n){
  var num_string = n.toString();
  
  var reverse = [];
  for(var i=(num_string.length)-1;i>=0;i--){
    reverse.push(num_string[i]);
    
  }
  var reverse_sort = reverse.sort()
  var res = reverse_sort.reverse().join('')
  
  return parseInt(res);
  
}