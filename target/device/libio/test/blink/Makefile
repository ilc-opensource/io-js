
all: configure build

configure:
	gyp --depth=. --generator-output=build

build:
	make -C build

clean:
	rm -rf build
	rm -rf ../libio*

.PHONY: configure build clean
