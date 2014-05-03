#include "fast_gpio_sc_addon.h"

// 26: int fastGpioSCInit ( void ) ;
Handle<Value> fastGpioSCInitV8(const Arguments &args) {
    HandleScope scope;
        
    int ret = fastGpioSCInit();
    
    return scope.Close(Int32::New((int)ret));
}
// 27: void fastGpioSCFini ( void ) ;
Handle<Value> fastGpioSCFiniV8(const Arguments &args) {
    HandleScope scope;
        
    fastGpioSCFini();
    
    return scope.Close(Undefined());
    
}
// 28: void fastGpioDigitalWrite ( register uint8_t gpio , register uint8_t val ) ;
Handle<Value> fastGpioDigitalWriteV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    unsigned int arg1 = (unsigned int)args[1]->Uint32Value();
        
    fastGpioDigitalWrite(arg0, arg1);
    
    return scope.Close(Undefined());
    
}
// 29: void fastGpioDigitalWriteDestructive ( register uint8_t gpio ) ;
Handle<Value> fastGpioDigitalWriteDestructiveV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
        
    fastGpioDigitalWriteDestructive(arg0);
    
    return scope.Close(Undefined());
    
}
// 30: uint32_t fastGpioDigitalLatch ( void ) ;
Handle<Value> fastGpioDigitalLatchV8(const Arguments &args) {
    HandleScope scope;
        
    unsigned int ret = fastGpioDigitalLatch();
    
    return scope.Close(Uint32::New((unsigned int)ret));
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

static void SetConst(Handle<Object> obj) {

}
void Initfast_gpio_sc(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);
}
