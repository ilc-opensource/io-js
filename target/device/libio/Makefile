build:
	node-gyp build

rebuild:
	node-gyp rebuild --arch=ia32

configure:
	node-gyp configure --arch=ia32

clean:
	node-gyp clean
	rm -rf build export
	make -C test clean

.PHONY: build rebuild configure clean
