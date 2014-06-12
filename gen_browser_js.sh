OUTPUT=bundle.js
ROOT=.

FILE="$ROOT/target/companion/lib/jquery/jay_jquery.js"
echo $FILE
cat $FILE > $OUTPUT

FILE="$ROOT/target/companion/lib/browser_init.js"
echo $FILE
cat $FILE >> $OUTPUT

FILE="$ROOT/target/companion/lib/utils.js"
echo $FILE
cat $FILE >> $OUTPUT

FILE="$ROOT/target/companion/lib/submit/rpc.js"
echo $FILE
cat $FILE >> $OUTPUT

FILE="$ROOT/target/companion/lib/submit/print.js"
echo $FILE
cat $FILE >> $OUTPUT

FILE="$ROOT/target/companion/lib/board/galileo.js"
echo $FILE
cat $FILE >> $OUTPUT

FILE="$ROOT/target/companion/index.js"
echo $FILE
cat $FILE >> $OUTPUT

FILE="$ROOT/target/common/led.js"
echo $FILE
cat $FILE >> $OUTPUT

FILE="$ROOT/target/common/index.js"
echo $FILE
cat $FILE >> $OUTPUT

FILE="$ROOT/target/index.js"
echo $FILE
cat $FILE >> $OUTPUT
