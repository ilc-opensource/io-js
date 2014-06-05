ROOT_DIR = $(shell pwd)

all: configure rebuild

configure:
	make -C $(ROOT_DIR)/target/device/libio clean
	make -C $(ROOT_DIR)/target/device/libio rebuild
 
rebuild:
	make -C $(ROOT_DIR)/utils/autogen/      run 
	make -C $(ROOT_DIR)/target/device/board rebuild
	./gen_browser_js.sh

build:
	make -C $(ROOT_DIR)/utils/autogen/      run 
	make -C $(ROOT_DIR)/target/device/board build
	./gen_browser_js.sh

clean:
	make -C $(ROOT_DIR)/target/device/libio clean
	make -C $(ROOT_DIR)/target/device/board clean
	make -C $(ROOT_DIR)/utils/autogen/      clean

test:
	buster-test

.PHONY: configure build
