var Board = require(__dirname + '/lib/board/galileo.js').Board

var board = new Board({submitPath: __dirname + '/lib/submit/print.js'});

module.exports = board;
