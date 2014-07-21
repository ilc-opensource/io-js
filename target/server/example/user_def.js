var Foo = function(s) {
  console.log('hello ' + s);
};

if(isRpcServer) {
  exports.RPC = {
    'myFun': Foo
  };
}

