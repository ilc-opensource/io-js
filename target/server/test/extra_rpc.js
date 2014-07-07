if(isRpcServer) {
  exports.RPC = {
    'abc': function(){
      console.log('abc');
      return 'ABC';
    },
    'hello': function(){
      console.log('hello');
      return 'HELLO';
    },
  };
}
