#include "UtilTime_addon.h"

// 11: unsigned long millis ( void ) ;
Handle<Value> millisV8(const Arguments &args) {
    HandleScope scope;
        
    unsigned int ret = millis();
    
    return scope.Close(Uint32::New((unsigned int)ret));
}
// 12: unsigned long micros ( void ) ;
Handle<Value> microsV8(const Arguments &args) {
    HandleScope scope;
        
    unsigned int ret = micros();
    
    return scope.Close(Uint32::New((unsigned int)ret));
}
// 13: void delay ( unsigned long ) ;
Handle<Value> delayV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
        
    delay(arg0);
    
    return scope.Close(Undefined());
    
}
// 14: void delayMicroseconds ( unsigned int us ) ;
Handle<Value> delayMicrosecondsV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
        
    delayMicroseconds(arg0);
    
    return scope.Close(Undefined());
    
}
static void SetMemberFunc(Handle<Object> obj) {
    obj->Set(v8::String::NewSymbol("millis"),
           FunctionTemplate::New(millisV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("micros"),
           FunctionTemplate::New(microsV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("delay"),
           FunctionTemplate::New(delayV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("delayMicroseconds"),
           FunctionTemplate::New(delayMicrosecondsV8)->GetFunction());
}

static void SetConst(Handle<Object> obj) {

}
void InitUtilTime(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);
}
