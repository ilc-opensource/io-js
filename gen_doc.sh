#Install:
#  npm install jsdoc
#  git clone https://github.com/davidshimjs/jaguarjs-jsdoc

DOC=./doc
rm -rf $DOC
mkdir $DOC

EXTRA_OPTION=""
if [ -d '../jaguarjs-jsdoc' ]; then
  EXTRA_OPTION='-t ../jaguarjs-jsdoc/ -c ./doc-conf.json' 
fi

FILES='
  ./target/companion/lib/board/galileo.js
  ./target/companion/index.js
  ./target/extension/led.js 
'
RUN="jsdoc -d $DOC $EXTRA_OPTION $* $FILES"
echo $RUN
$RUN
