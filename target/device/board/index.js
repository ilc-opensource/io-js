
var IO = require('bindings')('galileo.node');

var Board = function() {
  this.hello = 'world';

};

Board.prototype = IO;

Board.prototype.config = function(options) {
};

var board = new Board();

exports.Board = Board; 
