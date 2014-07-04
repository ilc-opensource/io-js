# !/bin/bash
home_dir=`pwd`
echo $home_dir
cd $home_dir/utils/autogen
python run.py autogen_test
cd $home_dir/target/device/
node-gyp configure build
cd $home_dir/utils/autogen/testSuite
node test_autogen.js

