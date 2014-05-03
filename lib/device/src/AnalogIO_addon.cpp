#include "AnalogIO_addon.h"

// 19: void pwmInit ( void ) ;
Handle<Value> pwmInitV8(const Arguments &args) {
    HandleScope scope;
        
    pwmInit();
    
    return scope.Close(Undefined());
    
}
// 20: uint32_t analogRead ( uint32_t ) ;
Handle<Value> analogReadV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
        
    unsigned int ret = analogRead(arg0);
    
    return scope.Close(Uint32::New((unsigned int)ret));
}
// 21: void analogReadResolution ( uint32_t res ) ;
Handle<Value> analogReadResolutionV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
        
    analogReadResolution(arg0);
    
    return scope.Close(Undefined());
    
}
// 22: void analogReference ( uint8_t mode ) ;
Handle<Value> analogReferenceV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
        
    analogReference(arg0);
    
    return scope.Close(Undefined());
    
}
// 23: void analogWrite ( uint32_t , uint32_t ) ;
Handle<Value> analogWriteV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    unsigned int arg1 = (unsigned int)args[1]->Uint32Value();
        
    analogWrite(arg0, arg1);
    
    return scope.Close(Undefined());
    
}
// 25: int pin2pwmhandle_enable ( uint8_t pin ) ;
Handle<Value> pin2pwmhandle_enableV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
        
    int ret = pin2pwmhandle_enable(arg0);
    
    return scope.Close(Int32::New((int)ret));
}
static void SetMemberFunc(Handle<Object> obj) {
    obj->Set(v8::String::NewSymbol("pwmInit"),
           FunctionTemplate::New(pwmInitV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("analogRead"),
           FunctionTemplate::New(analogReadV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("analogReadResolution"),
           FunctionTemplate::New(analogReadResolutionV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("analogReference"),
           FunctionTemplate::New(analogReferenceV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("analogWrite"),
           FunctionTemplate::New(analogWriteV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("pin2pwmhandle_enable"),
           FunctionTemplate::New(pin2pwmhandle_enableV8)->GetFunction());
}

static void SetConst(Handle<Object> obj) {

}
void InitAnalogIO(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);
}
