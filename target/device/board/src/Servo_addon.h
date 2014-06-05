
#ifndef SERVO_ADDON_H
#define SERVO_ADDON_H

#include <node.h>
#include <v8.h>
#include "Servo.h"

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



class ServoV8: public node::ObjectWrap {

private:
    Servo *m_val;
    ~ServoV8() { };
    static v8::Handle<v8::Value> New(const v8::Arguments& args);
    static v8::Persistent<v8::Function> constructor;

public:
    static void Init(v8::Handle<v8::Object> exports);
    explicit ServoV8();

    static v8::Handle<v8::Value> attachV8(const v8::Arguments& args);
    static v8::Handle<v8::Value> detachV8(const v8::Arguments& args);
    static v8::Handle<v8::Value> writeV8(const v8::Arguments& args);
    static v8::Handle<v8::Value> writeMicrosecondsV8(const v8::Arguments& args);
    static v8::Handle<v8::Value> readV8(const v8::Arguments& args);
    static v8::Handle<v8::Value> readMicrosecondsV8(const v8::Arguments& args);
    static v8::Handle<v8::Value> attachedV8(const v8::Arguments& args);
    static v8::Handle<v8::Value> set48hzV8(const v8::Arguments& args);
    static v8::Handle<v8::Value> set188hzV8(const v8::Arguments& args);
};

#endif