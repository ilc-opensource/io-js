var IO = require('./globalClassVarSetterGetter');

var Board = function() {
  this.hello = 'world';

};

Board.prototype = IO;

Board.prototype.config = function(options) {
};

var board = new Board();

exports.Board = Board; 
