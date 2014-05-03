#include "wiring_digital_norm_addon.h"

// 34: void pinInit ( void ) ;
Handle<Value> pinInitV8(const Arguments &args) {
    HandleScope scope;
        
    pinInit();
    
    return scope.Close(Undefined());
    
}
// 35: void pinMode ( uint8_t pin , uint8_t mode ) ;
Handle<Value> pinModeV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    unsigned int arg1 = (unsigned int)args[1]->Uint32Value();
        
    pinMode(arg0, arg1);
    
    return scope.Close(Undefined());
    
}
// 36: int pinModeIRQ ( uint8_t pin , int8_t mode ) ;
Handle<Value> pinModeIRQV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsInt32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    int arg1 = (int)args[1]->IntegerValue();
        
    int ret = pinModeIRQ(arg0, arg1);
    
    return scope.Close(Int32::New((int)ret));
}
// 37: void digitalWrite ( register uint8_t pin , register uint8_t val ) ;
Handle<Value> digitalWriteV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    unsigned int arg1 = (unsigned int)args[1]->Uint32Value();
        
    digitalWrite(arg0, arg1);
    
    return scope.Close(Undefined());
    
}
// 38: int digitalRead ( uint8_t pin ) ;
Handle<Value> digitalReadV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
        
    int ret = digitalRead(arg0);
    
    return scope.Close(Int32::New((int)ret));
}
// 42: int pinHandleReopen ( uint8_t index ) ;
Handle<Value> pinHandleReopenV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
        
    int ret = pinHandleReopen(arg0);
    
    return scope.Close(Int32::New((int)ret));
}
// 43: int pinGetIndex ( uint8_t pin ) ;
Handle<Value> pinGetIndexV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
        
    int ret = pinGetIndex(arg0);
    
    return scope.Close(Int32::New((int)ret));
}
// 44: char * pin2path ( uint8_t pin ) ;
Handle<Value> pin2pathV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
        
    char* ret = pin2path(arg0);
    
    return scope.Close(v8::String::New((char*)ret));
}
// 45: int gpio2gpiohandle ( uint32_t gpio ) ;
Handle<Value> gpio2gpiohandleV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
        
    int ret = gpio2gpiohandle(arg0);
    
    return scope.Close(Int32::New((int)ret));
}
// 46: int pin2gpiohandle ( uint8_t pin ) ;
Handle<Value> pin2gpiohandleV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
        
    int ret = pin2gpiohandle(arg0);
    
    return scope.Close(Int32::New((int)ret));
}
static void SetMemberFunc(Handle<Object> obj) {
    obj->Set(v8::String::NewSymbol("pinInit"),
           FunctionTemplate::New(pinInitV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("pinMode"),
           FunctionTemplate::New(pinModeV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("pinModeIRQ"),
           FunctionTemplate::New(pinModeIRQV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("digitalWrite"),
           FunctionTemplate::New(digitalWriteV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("digitalRead"),
           FunctionTemplate::New(digitalReadV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("pinHandleReopen"),
           FunctionTemplate::New(pinHandleReopenV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("pinGetIndex"),
           FunctionTemplate::New(pinGetIndexV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("pin2path"),
           FunctionTemplate::New(pin2pathV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("gpio2gpiohandle"),
           FunctionTemplate::New(gpio2gpiohandleV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("pin2gpiohandle"),
           FunctionTemplate::New(pin2gpiohandleV8)->GetFunction());
}

static void SetConst(Handle<Object> obj) {

    obj->Set(v8::String::NewSymbol("HIGH"),
             Int32::New(0x1));

    obj->Set(v8::String::NewSymbol("LOW"),
             Int32::New(0x0));

    obj->Set(v8::String::NewSymbol("NONE"),
             Int32::New(0xFFFFFFFF));

    obj->Set(v8::String::NewSymbol("FN_GPIO_FIXED_OUTPUT"),
             Int32::New(0x02));

    obj->Set(v8::String::NewSymbol("FN_GPIO_OPENDRAIN"),
             Int32::New(0x04));

    obj->Set(v8::String::NewSymbol("FN_PWM"),
             Int32::New(0x08));

    obj->Set(v8::String::NewSymbol("FN_I2C"),
             Int32::New(0x10));

    obj->Set(v8::String::NewSymbol("FN_ANALOG"),
             Int32::New(0x20));

    obj->Set(v8::String::NewSymbol("FN_UART"),
             Int32::New(0x40));

    obj->Set(v8::String::NewSymbol("FN_SPI"),
             Int32::New(0x80));

    obj->Set(v8::String::NewSymbol("FN_PULLUP"),
             Int32::New(0x100));

    obj->Set(v8::String::NewSymbol("FN_MUX"),
             Int32::New(0x200));

    obj->Set(v8::String::NewSymbol("FN_RESERVED"),
             Int32::New(0x400));

    obj->Set(v8::String::NewSymbol("GPIO_DRIVE_PULLUP"),
             Int32::New(0));

    obj->Set(v8::String::NewSymbol("GPIO_DRIVE_STRONG"),
             Int32::New(1));

    obj->Set(v8::String::NewSymbol("GPIO_DRIVE_HIZ"),
             Int32::New(2));

    obj->Set(v8::String::NewSymbol("PIN_EINVAL"),
             Int32::New(0xFFFFFFFF));

    obj->Set(v8::String::NewSymbol("MAX_GPIO_PATH"),
             Int32::New(0x200));

}
void Initwiring_digital_norm(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);
}
