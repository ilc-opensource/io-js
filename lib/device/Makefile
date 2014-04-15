ARDUINO_REL_PATH =../../../arduino-1.5.3
ARCH = $(shell uname -m)
ARDUINO_PATH = $(shell pwd)/$(ARDUINO_REL_PATH)
SYSROOT=$(ARDUINO_PATH)/hardware/tools/sysroots/i586-poky-linux-uclibc
export CC=$(ARDUINO_PATH)/hardware/tools/sysroots/$(ARCH)-pokysdk-linux/usr/bin/i586-poky-linux-uclibc/i586-poky-linux-uclibc-gcc --sysroot=$(SYSROOT) -m32 -march=i586 -w -ffunction-sections -f data-sections -MMD -DARDUINO=153
export CXX=$(ARDUINO_PATH)/hardware/tools/sysroots/$(ARCH)-pokysdk-linux/usr/bin/i586-poky-linux-uclibc/i586-poky-linux-uclibc-g++ --sysroot=$(SYSROOT) -m32 -march=i586 -w -fno-exceptions -ffunction-sections -fdata-sections -DARDUINO=153
export LINK=$(ARDUINO_PATH)/hardware/tools/sysroots/$(ARCH)-pokysdk-linux/usr/bin/i586-poky-linux-uclibc/i586-poky-linux-uclibc-g++ --sysroot=$(SYSROOT)

GYP_MAKE = build/Makefile
GYP_FLAGS = --arch=ia32 --target=0.8.18

all: configure build

build:
	node-gyp build

$(GYP_MAKE):
	node-gyp configure $(GYP_FLAGS)

configure: $(GYP_MAKE)

clean:
	rm -rf build

.PHONY: all build init 
