#include "fast_gpio_sc_addon.h"
#include "stdlib.h"
#include "string.h"
#include "_callback.h"

// 26: int fastGpioSCInit ( void ) ;
Handle<Value> fastGpioSCInitV8(const Arguments &args) {
    HandleScope scope;
        
    // Call C++ function
    int ret = fastGpioSCInit();
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 27: void fastGpioSCFini ( void ) ;
Handle<Value> fastGpioSCFiniV8(const Arguments &args) {
    HandleScope scope;
        
    // Call C++ function
    fastGpioSCFini();
    
    return scope.Close(Undefined());
    
}
// 28: void fastGpioDigitalWrite ( register uint8_t gpio , register uint8_t val ) ;
Handle<Value> fastGpioDigitalWriteV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    register uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
    register uint8_t arg1 = (uint8_t)args[1]->Uint32Value();
    
        
    // Call C++ function
    fastGpioDigitalWrite(arg0, arg1);
    
    return scope.Close(Undefined());
    
}
// 29: void fastGpioDigitalWriteDestructive ( register uint8_t gpio ) ;
Handle<Value> fastGpioDigitalWriteDestructiveV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    register uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
        
    // Call C++ function
    fastGpioDigitalWriteDestructive(arg0);
    
    return scope.Close(Undefined());
    
}
// 30: uint32_t fastGpioDigitalLatch ( void ) ;
Handle<Value> fastGpioDigitalLatchV8(const Arguments &args) {
    HandleScope scope;
        
    // Call C++ function
    unsigned int ret = fastGpioDigitalLatch();
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Uint32::New((unsigned int)ret);
    
    return scope.Close(retV8);
}
static void SetMemberFunc(Handle<Object> obj) {
    obj->Set(v8::String::NewSymbol("fastGpioSCInit"),
           FunctionTemplate::New(fastGpioSCInitV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("fastGpioSCFini"),
           FunctionTemplate::New(fastGpioSCFiniV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("fastGpioDigitalWrite"),
           FunctionTemplate::New(fastGpioDigitalWriteV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("fastGpioDigitalWriteDestructive"),
           FunctionTemplate::New(fastGpioDigitalWriteDestructiveV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("fastGpioDigitalLatch"),
           FunctionTemplate::New(fastGpioDigitalLatchV8)->GetFunction());
}


// Const defined by macros
static void SetConst(Handle<Object> obj) {

}

// Const defined by enumeration
static void SetEnumConst(Handle<Object> obj) {

}
static void SetGlobalVarFunc(Handle<Object> obj) {
}

void Initfast_gpio_sc(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);

    SetEnumConst(exports);

    SetGlobalVarFunc(exports);
}
