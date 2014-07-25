
var IOLIB = require('../');

var io = new IOLIB.IO({
  log: true,
  quickInit: false
});

var data = [0,68,68,68,68,20,68,0,0,68,68,20,65,20,68,0,0,68,68,17,17,20,68,0,0,68,20,1,16,17,68,0,0,68,17,0,0,17,68,0,0,20,1,0,0,16,65,0,0,17,0,17,17,0,17,0,0,18,0,1,16,0,33,0,0,18,0,1,16,0,33,0,0,18,0,1,16,0,33,0,0,18,0,1,16,0,33,0,0,18,17,17,17,17,33,0];

var handle = io.mug_init();

io.mug_disp_img_N(handle, "test.bmp", 30);

io.mug_disp_raw(handle, data);

io.mug_close(handle);
