codes = {
  'unkown' : 1,
  'offload' : 2,
};

module.exports = {
  log : console.log,
  genErr: function(type, message) {
    var code = codes[type];
    
    if(code === undefined) {
      code = codes['unkown'];
    }

    return {
      code : code, 
      message: type + ' error: ' + message
    };

  },
}
