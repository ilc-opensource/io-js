#Install:
#  npm install jsdoc

DOC=./doc
TEMPLATE=./lib/jaguarjs-jsdoc
rm -rf $DOC
mkdir $DOC

EXTRA_OPTION=""
if [ -d "$TEMPLATE" ]; then
  EXTRA_OPTION="-t $TEMPLATE -c ./doc-conf.json"
fi

FILES='
  ./target/companion/lib/board/galileo.js
  ./target/companion/index.js
  ./target/extension/led.js 
'
RUN="jsdoc -d $DOC $EXTRA_OPTION $* $FILES ./README.md"
echo $RUN
$RUN
