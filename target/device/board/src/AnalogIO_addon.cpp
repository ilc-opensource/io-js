#include "AnalogIO_addon.h"
#include "stdlib.h"
#include "string.h"
#include "_callback.h"

// 19: void pwmInit ( void ) ;
Handle<Value> pwmInitV8(const Arguments &args) {
    HandleScope scope;
        
    // Call C++ function
    pwmInit();
    
    return scope.Close(Undefined());
    
}
// 20: uint32_t analogRead ( uint32_t ) ;
Handle<Value> analogReadV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint32_t arg0 = (uint32_t)args[0]->Uint32Value();
    
        
    // Call C++ function
    unsigned int ret = analogRead(arg0);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Uint32::New((unsigned int)ret);
    
    return scope.Close(retV8);
}
// 21: void analogReadResolution ( uint32_t res ) ;
Handle<Value> analogReadResolutionV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint32_t arg0 = (uint32_t)args[0]->Uint32Value();
    
        
    // Call C++ function
    analogReadResolution(arg0);
    
    return scope.Close(Undefined());
    
}
// 22: void analogReference ( uint8_t mode ) ;
Handle<Value> analogReferenceV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
        
    // Call C++ function
    analogReference(arg0);
    
    return scope.Close(Undefined());
    
}
// 23: void analogWrite ( uint32_t , uint32_t ) ;
Handle<Value> analogWriteV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint32_t arg0 = (uint32_t)args[0]->Uint32Value();
    
    uint32_t arg1 = (uint32_t)args[1]->Uint32Value();
    
        
    // Call C++ function
    analogWrite(arg0, arg1);
    
    return scope.Close(Undefined());
    
}
// 25: int pin2pwmhandle_enable ( uint8_t pin ) ;
Handle<Value> pin2pwmhandle_enableV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
        
    // Call C++ function
    int ret = pin2pwmhandle_enable(arg0);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
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


// Const defined by macros
static void SetConst(Handle<Object> obj) {

}

// Const defined by enumeration
static void SetEnumConst(Handle<Object> obj) {

}
static void SetGlobalVarFunc(Handle<Object> obj) {
}

void InitAnalogIO(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);

    SetEnumConst(exports);

    SetGlobalVarFunc(exports);
}
