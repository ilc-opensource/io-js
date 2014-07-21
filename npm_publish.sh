ROOT=$PWD
echo "Please call 'npm adduser' to setup user info"
npm_publish() {
  DIR=$1
  echo "publishing $DIR"

  cp -r $ROOT/doc $DIR/
  cp -r $ROOT/target/extension $DIR/

  cd $DIR
  make clean
  npm publish 

  cd $ROOT
  rm -r $DIR/doc
  rm -r $DIR/extension
}

npm_publish target/device;
npm_publish target/server;
npm_publish target/companion;

