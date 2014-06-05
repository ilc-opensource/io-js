#include "pins_arduino_addon.h"
#include "stdlib.h"
#include "string.h"
#include "_callback.h"

static void SetMemberFunc(Handle<Object> obj) {}


// Const defined by macros
static void SetConst(Handle<Object> obj) {

    obj->Set(v8::String::NewSymbol("NUM_DIGITAL_PINS"),
             Int32::New(20));

    obj->Set(v8::String::NewSymbol("NUM_ANALOG_INPUTS"),
             Int32::New(6));

    obj->Set(v8::String::NewSymbol("NUM_UARTS"),
             Int32::New(0x03));

    obj->Set(v8::String::NewSymbol("NUM_SPI"),
             Int32::New(0x02));

    obj->Set(v8::String::NewSymbol("NUM_I2C"),
             Int32::New(0x01));

}

// Const defined by enumeration
static void SetEnumConst(Handle<Object> obj) {

}

// Setter and Getter function for global variable
Handle<Value> GetSsV8(const v8::Arguments &args) {
    HandleScope scope;

    Handle<Value> SSV8 = Uint32::New((unsigned int)SS);
    
    return scope.Close(SSV8);
}
Handle<Value> GetMosiV8(const v8::Arguments &args) {
    HandleScope scope;

    Handle<Value> MOSIV8 = Uint32::New((unsigned int)MOSI);
    
    return scope.Close(MOSIV8);
}
Handle<Value> GetMisoV8(const v8::Arguments &args) {
    HandleScope scope;

    Handle<Value> MISOV8 = Uint32::New((unsigned int)MISO);
    
    return scope.Close(MISOV8);
}
Handle<Value> GetSckV8(const v8::Arguments &args) {
    HandleScope scope;

    Handle<Value> SCKV8 = Uint32::New((unsigned int)SCK);
    
    return scope.Close(SCKV8);
}
Handle<Value> GetSdaV8(const v8::Arguments &args) {
    HandleScope scope;

    Handle<Value> SDAV8 = Uint32::New((unsigned int)SDA);
    
    return scope.Close(SDAV8);
}
Handle<Value> GetSclV8(const v8::Arguments &args) {
    HandleScope scope;

    Handle<Value> SCLV8 = Uint32::New((unsigned int)SCL);
    
    return scope.Close(SCLV8);
}
Handle<Value> GetLed_builtinV8(const v8::Arguments &args) {
    HandleScope scope;

    Handle<Value> LED_BUILTINV8 = Uint32::New((unsigned int)LED_BUILTIN);
    
    return scope.Close(LED_BUILTINV8);
}
Handle<Value> GetA0V8(const v8::Arguments &args) {
    HandleScope scope;

    Handle<Value> A0V8 = Uint32::New((unsigned int)A0);
    
    return scope.Close(A0V8);
}
Handle<Value> GetA1V8(const v8::Arguments &args) {
    HandleScope scope;

    Handle<Value> A1V8 = Uint32::New((unsigned int)A1);
    
    return scope.Close(A1V8);
}
Handle<Value> GetA2V8(const v8::Arguments &args) {
    HandleScope scope;

    Handle<Value> A2V8 = Uint32::New((unsigned int)A2);
    
    return scope.Close(A2V8);
}
Handle<Value> GetA3V8(const v8::Arguments &args) {
    HandleScope scope;

    Handle<Value> A3V8 = Uint32::New((unsigned int)A3);
    
    return scope.Close(A3V8);
}
Handle<Value> GetA4V8(const v8::Arguments &args) {
    HandleScope scope;

    Handle<Value> A4V8 = Uint32::New((unsigned int)A4);
    
    return scope.Close(A4V8);
}
Handle<Value> GetA5V8(const v8::Arguments &args) {
    HandleScope scope;

    Handle<Value> A5V8 = Uint32::New((unsigned int)A5);
    
    return scope.Close(A5V8);
}
Handle<Value> GetA6V8(const v8::Arguments &args) {
    HandleScope scope;

    Handle<Value> A6V8 = Uint32::New((unsigned int)A6);
    
    return scope.Close(A6V8);
}
Handle<Value> GetA7V8(const v8::Arguments &args) {
    HandleScope scope;

    Handle<Value> A7V8 = Uint32::New((unsigned int)A7);
    
    return scope.Close(A7V8);
}

static void SetGlobalVarFunc(Handle<Object> obj) {

    obj->Set(v8::String::NewSymbol("getSsV8"),
           FunctionTemplate::New(GetSsV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("getMosiV8"),
           FunctionTemplate::New(GetMosiV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("getMisoV8"),
           FunctionTemplate::New(GetMisoV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("getSckV8"),
           FunctionTemplate::New(GetSckV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("getSdaV8"),
           FunctionTemplate::New(GetSdaV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("getSclV8"),
           FunctionTemplate::New(GetSclV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("getLed_builtinV8"),
           FunctionTemplate::New(GetLed_builtinV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("getA0V8"),
           FunctionTemplate::New(GetA0V8)->GetFunction());

    obj->Set(v8::String::NewSymbol("getA1V8"),
           FunctionTemplate::New(GetA1V8)->GetFunction());

    obj->Set(v8::String::NewSymbol("getA2V8"),
           FunctionTemplate::New(GetA2V8)->GetFunction());

    obj->Set(v8::String::NewSymbol("getA3V8"),
           FunctionTemplate::New(GetA3V8)->GetFunction());

    obj->Set(v8::String::NewSymbol("getA4V8"),
           FunctionTemplate::New(GetA4V8)->GetFunction());

    obj->Set(v8::String::NewSymbol("getA5V8"),
           FunctionTemplate::New(GetA5V8)->GetFunction());

    obj->Set(v8::String::NewSymbol("getA6V8"),
           FunctionTemplate::New(GetA6V8)->GetFunction());

    obj->Set(v8::String::NewSymbol("getA7V8"),
           FunctionTemplate::New(GetA7V8)->GetFunction());
}

void Initpins_arduino(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);

    SetEnumConst(exports);

    SetGlobalVarFunc(exports);
}
