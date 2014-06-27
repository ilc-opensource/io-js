ROOT_DIR = $(shell pwd)

all: configure rebuild

configure:
	make -C $(ROOT_DIR)/target/device/libio clean
	make -C $(ROOT_DIR)/target/device/libio rebuild
 
rebuild:
	make -C $(ROOT_DIR)/utils/autogen/      run 
	make -C $(ROOT_DIR)/target/device/      rebuild
	./gen_browser_js.sh

build:
	make -C $(ROOT_DIR)/utils/autogen/      run 
	make -C $(ROOT_DIR)/target/device       build
	./gen_browser_js.sh

clean:
	make -C $(ROOT_DIR)/target/device/libio clean
	make -C $(ROOT_DIR)/target/device       clean
	make -C $(ROOT_DIR)/utils/autogen/      clean
	./gen_browser_js.sh -c

test:
	buster-test

.PHONY: configure build
