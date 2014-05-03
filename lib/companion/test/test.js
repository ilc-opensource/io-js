//var io =require('./io_rpc.js');
var io =require('../io_fake.js');

io.config();
io.digitalRead(1, 2);
