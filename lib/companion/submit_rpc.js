var jayson = require('jayson');
var utils = require('./utils.js');

var client = jayson.client.http({
  port: 2000,
  hostname: 'localhost'
});

module.exports = {

  'classReq' : function(className, args) {

    var self = this;

    client.request('%s', utils.toArray(args), function(error, response) {
      self.rpcid = response.rpcid;
    });

  },

  'classMethodReq': function(className, methodName, args) {

    // attach rpcid
    args.push(this.rpcid);

    client.request(className + '.' + methodName, utils.toArray(args), function(error, response) {
      console.log(response);
    });
        
  },

  'funcReq' : function(funcName, args) {

    client.request(funcName, utils.toArray(args), function(error, response) {
      console.log(response);
    });
  }

};
