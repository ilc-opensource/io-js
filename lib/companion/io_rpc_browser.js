this.io = new Board();

// function: convert string to integer array
// Used for mapping char* in C/C++ to JS
// Example: strToIntArray("hello")
var strToIntArray = function(str) {
  intArr = [];
  for (i = 0; i < str.length; i++) {
    intArr[i] = str.charCodeAt(i);
  }
  return intArr;
}

// function: convert integer array to string
var intArrayToStr = function(intArr) {
  str = "";
  for (i = 0; i < intArr.length; i++) {
    str += String.fromCharCode(intArr[i]);
  }
  return str;
}
