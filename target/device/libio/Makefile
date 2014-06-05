build:
	node-gyp build

rebuild:
	node-gyp rebuild

configure:
	node-gyp configure

clean:
	node-gyp clean
	rm -rf build export
	make -C test clean

.PHONY: build rebuild configure clean
