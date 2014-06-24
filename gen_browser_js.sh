OUTPUT=bundle.js
ROOT=.

while getopts o:lc option
do
    case "$option" in
        o)
            OUTPUT=$OPTARG;;
        c)
            echo "clean $OUTPUT"
            rm -rf $OUTPUT
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

echo "creating $OUTPUT" 

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
