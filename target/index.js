(function(exports, global) {

  exports.IO = function(config) {
    var IOObj;

    //Initialize default configu
    config.log = config.log || false;
    if(config.quickInit == undefined)
      config.quickInit = true;         
    
    if(config.emu || config.fake || config.rpc) {
      IOObj = (typeof require === 'function') ? 
                require('./companion/').Companion
              : global.Companion;
    } else {
      if(typeof require !== 'function')
        throw 'Not allowed in Browser, forgot to set rpc?';
      IOObj = require('./device/board').Board;
    }

    this.test = 'hello';
    
    var temp = new IOObj(config);
    for(idx in temp)
      this[idx] = temp[idx];
   
    IOObj.call(this, config); 
   
    // configuration
    this.config(config);    
    
    // initializee ttys, it will effect serial.write/read
    var ttys = [];
    if(config.tty != undefined) {
      ttys[0] = config.tty;
      ttys[1] = config.tty;
      ttys[2] = config.tty;      
    } else {
      ttys = ["/dev/tty", "/dev/tty", "/dev/tty"];
    }
    
    if(config.quickInit) {     
      this.initWithTty.apply(null, ttys);
    }
    
  };
  
// Merge high level APIs into this interface
var common = (typeof require === 'function')? 
             require('./common/').HighLevel
           : global.HighLevel

for(idx in common) {
  exports[idx] = common[idx];
}

})(typeof exports === 'object'? module.exports: this.IOLIB, this.IOLIB);
