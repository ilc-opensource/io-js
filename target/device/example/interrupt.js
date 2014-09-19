var IOLIB = require('../');

var io = new IOLIB.IO({
  log: true,
});

io.interrupt_init(1000); 

var irq_callback = function() 
{
  console.log("!!!!!!!!!!!!!!!!!!!!!!!!!in interrupt."); 
} 

io.pinMode(2,1); 
io.digitalWrite(2,0); 
io.attachInterrupt(2, irq_callback, 8); 
io.digitalWrite(2,1);
