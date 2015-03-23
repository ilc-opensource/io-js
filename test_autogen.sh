# !/bin/bash
home_dir=`pwd`

cd $home_dir/utils/autogen
python run.py -t

if [ $? -ne 0 ]; then
  exit 1
fi

cd $home_dir/target/device/
node-gyp configure build

if [ $? -ne 0 ]; then
  exit 1
fi

cd $home_dir/utils/autogen/testSuite
node test_autogen.js

