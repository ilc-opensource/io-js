
#ifndef ANALOGIO_ADDON_H
#define ANALOGIO_ADDON_H

#include <node.h>
#include <v8.h>
#include "AnalogIO.h"

using namespace v8;

#ifndef V8_EXCEPTION
#define V8_EXCEPTION(info) { \
    v8::ThrowException(Exception::Error(v8::String::New(info))); \
    }
#endif

#ifndef V8_ASSERT
#define V8_ASSERT(cond, ...) \
    if(!(cond)) {  \
        char buffer[512]; \
        sprintf(buffer, __VA_ARGS__); \
        V8_EXCEPTION(buffer); \
        return scope.Close(Undefined()); \
    }
#endif



#endif