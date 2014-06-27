
TARGET_DIR=.
ROOT=.
NAME=iotio
VER=general
OUTPUT=$NAME-$VER.js
OUTPUT_MINI=$NAME-$VER.mini.js
while getopts v:o:d:lc option
do
    case "$option" in
        v)
            VER=$OPTARG;;
        o)
            NAME=$OPTARG;;
        d)  TARGET_DIR=$OPTARG;;
        c)
            echo "rm -rf  $TARGET_DIR/$OUTPUT $TARGET_DIR/$OUTPUT_MINI"
            rm -rf  $TARGET_DIR/$OUTPUT $TARGET_DIR/$OUTPUT_MINI
            exit 0;;
        \?)
            echo ""
            echo "Merge all of Javascript library into a single file"
            echo ""
            echo "  -o  target_filename [default: ./bundle.js] "
            echo "  -c  clean default file"
            echo ""
            exit 1;;
    esac
done

NAME=$NAME
OUTPUT=$NAME-$VER.js
OUTPUT_MINI=$NAME-$VER.mini.js

echo "Generate a bundle Javascript file for browser"
echo "=============================="
echo "SRC ROOT:     $ROOT"
echo "TARGET DIR:   $TARGET_DIR"
echo "OUTPUT:       $OUTPUT"
echo "OUTPUT MINI:  $OUTPUT_MINI"
echo "=============================="

echo "// combined all of need libraries together with tools" > $OUTPUT

FILES="
  $ROOT/target/companion/lib/jquery/jay_jquery.js 
  $ROOT/target/companion/lib/browser_init.js
  $ROOT/target/companion/lib/utils.js
  $ROOT/target/companion/lib/submit/rpc.js
  $ROOT/target/companion/lib/submit/print.js
  $ROOT/target/companion/lib/board/galileo.js
  $ROOT/target/companion/index.js
  $ROOT/target/extension/led.js
  $ROOT/target/extension/index.js
  $ROOT/target/index.js
"

echo ""
echo "put below files into $TARGET_DIR/$OUTPUT"
echo ""

for f in $FILES
do
  echo $f
  cat "$f" >> $TARGET_DIR/$OUTPUT
done

echo ""
echo "verify tool"
TOOL=uglifyjs
which $TOOL
RET=$?

if [ $RET -eq 0 ]; then
  echo "translate to $TARGET_DIR/$OUTPUT_MINI" 
  $TOOL $TARGET_DIR/$OUTPUT > $TARGET_DIR/$OUTPUT_MINI 
  echo "OK" 
else
  echo "have not installed $TOOL, abort"
fi

