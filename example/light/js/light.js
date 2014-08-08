var imgOn = $('#on');
var imgOff = $('#off');
var isOn = false;

var disp = function(){
  if(isOn) {
    imgOn.show();
    imgOff.hide();
  } else {
    imgOn.hide();
    imgOff.show();
  }
}

imgOn.click(function(){
  toggle();
  disp();
});

imgOff.click(function(){
  toggle();
  disp();
});