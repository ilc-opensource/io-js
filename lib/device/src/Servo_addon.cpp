#include "Servo_addon.h"

Persistent<Function> ServoV8::constructor;

Handle<Value> ServoV8::New(const Arguments& args) {
    HandleScope scope;
 
  if ((args.Length() == 0)) {
    if (args.IsConstructCall()) {
      // Invoked as constructor: `new ServoV8(...)`
            
      ServoV8 *obj = new ServoV8();
      obj->Wrap(args.This());
      return args.This();
    } else {
      // Invoked as plain function `ServoV8(...)`, turn into construct call.
      const int argc = 0;
      Local<Value> argv[argc] = {  };
      return scope.Close(constructor->NewInstance(argc, argv));
    }
  }
}

// constructor
ServoV8::ServoV8() {
    m_val = new Servo();
}

// attach
Handle<Value> ServoV8::attachV8(const Arguments& args) {
    HandleScope scope;

    ServoV8* obj = ObjectWrap::Unwrap<ServoV8>(args.This());

    // 42: uint8_t attach ( int16_t pin ) ;
    if ((args.Length() == 1) && args[0]->IsInt32()) {
        
        V8_ASSERT(args[0]->IsInt32(), "parameters error!");
        
        int arg0 = (int)args[0]->IntegerValue();
        
        unsigned int ret = obj->m_val->attach(arg0);
        
        return scope.Close(Uint32::New((unsigned int)ret));
    }

    // 43: uint8_t attach ( int pin , int min , int max ) ;
    if ((args.Length() == 3) && args[0]->IsInt32() && args[1]->IsInt32() && args[2]->IsInt32()) {
        
        V8_ASSERT(args[0]->IsInt32() && args[1]->IsInt32() && args[2]->IsInt32(), "parameters error!");
        
        int arg0 = (int)args[0]->IntegerValue();
        int arg1 = (int)args[1]->IntegerValue();
        int arg2 = (int)args[2]->IntegerValue();
        
        unsigned int ret = obj->m_val->attach(arg0, arg1, arg2);
        
        return scope.Close(Uint32::New((unsigned int)ret));
    }

    V8_ASSERT(false, "parameters error!");

    return scope.Close(Undefined());
}

// 44: void detach ( ) ;
Handle<Value> ServoV8::detachV8(const Arguments& args) {
    HandleScope scope;

    ServoV8* obj = ObjectWrap::Unwrap<ServoV8>(args.This());
        
    obj->m_val->detach();
    
    return scope.Close(Undefined());
    
}
// 45: void write ( int val ) ;
Handle<Value> ServoV8::writeV8(const Arguments& args) {
    HandleScope scope;

    ServoV8* obj = ObjectWrap::Unwrap<ServoV8>(args.This());
    
    V8_ASSERT(args[0]->IsInt32(), "parameters error!");
    
    int arg0 = (int)args[0]->IntegerValue();
        
    obj->m_val->write(arg0);
    
    return scope.Close(Undefined());
    
}
// 46: void writeMicroseconds ( int value ) ;
Handle<Value> ServoV8::writeMicrosecondsV8(const Arguments& args) {
    HandleScope scope;

    ServoV8* obj = ObjectWrap::Unwrap<ServoV8>(args.This());
    
    V8_ASSERT(args[0]->IsInt32(), "parameters error!");
    
    int arg0 = (int)args[0]->IntegerValue();
        
    obj->m_val->writeMicroseconds(arg0);
    
    return scope.Close(Undefined());
    
}
// 47: int read ( ) ;
Handle<Value> ServoV8::readV8(const Arguments& args) {
    HandleScope scope;

    ServoV8* obj = ObjectWrap::Unwrap<ServoV8>(args.This());
        
    int ret = obj->m_val->read();
    
    return scope.Close(Int32::New((int)ret));
}
// 48: int readMicroseconds ( ) ;
Handle<Value> ServoV8::readMicrosecondsV8(const Arguments& args) {
    HandleScope scope;

    ServoV8* obj = ObjectWrap::Unwrap<ServoV8>(args.This());
        
    int ret = obj->m_val->readMicroseconds();
    
    return scope.Close(Int32::New((int)ret));
}
// 49: bool attached ( ) ;
Handle<Value> ServoV8::attachedV8(const Arguments& args) {
    HandleScope scope;

    ServoV8* obj = ObjectWrap::Unwrap<ServoV8>(args.This());
        
    bool ret = obj->m_val->attached();
    
    return scope.Close(Boolean::New((bool)ret));
}
// 50: void set48hz ( ) ;
Handle<Value> ServoV8::set48hzV8(const Arguments& args) {
    HandleScope scope;

    ServoV8* obj = ObjectWrap::Unwrap<ServoV8>(args.This());
        
    obj->m_val->set48hz();
    
    return scope.Close(Undefined());
    
}
// 51: void set188hz ( ) ;
Handle<Value> ServoV8::set188hzV8(const Arguments& args) {
    HandleScope scope;

    ServoV8* obj = ObjectWrap::Unwrap<ServoV8>(args.This());
        
    obj->m_val->set188hz();
    
    return scope.Close(Undefined());
    
}
void ServoV8::Init(Handle<Object> exports) {
    // Prepare constructor template
    Local<FunctionTemplate> tpl = FunctionTemplate::New(New);
    tpl->SetClassName(v8::String::NewSymbol("Servo"));
    tpl->InstanceTemplate()->SetInternalFieldCount(1);

    // Prototype 
    tpl->PrototypeTemplate()->Set(v8::String::NewSymbol("attach"),
        FunctionTemplate::New(attachV8)->GetFunction());

    tpl->PrototypeTemplate()->Set(v8::String::NewSymbol("detach"),
        FunctionTemplate::New(detachV8)->GetFunction());

    tpl->PrototypeTemplate()->Set(v8::String::NewSymbol("write"),
        FunctionTemplate::New(writeV8)->GetFunction());

    tpl->PrototypeTemplate()->Set(v8::String::NewSymbol("writeMicroseconds"),
        FunctionTemplate::New(writeMicrosecondsV8)->GetFunction());

    tpl->PrototypeTemplate()->Set(v8::String::NewSymbol("read"),
        FunctionTemplate::New(readV8)->GetFunction());

    tpl->PrototypeTemplate()->Set(v8::String::NewSymbol("readMicroseconds"),
        FunctionTemplate::New(readMicrosecondsV8)->GetFunction());

    tpl->PrototypeTemplate()->Set(v8::String::NewSymbol("attached"),
        FunctionTemplate::New(attachedV8)->GetFunction());

    tpl->PrototypeTemplate()->Set(v8::String::NewSymbol("set48hz"),
        FunctionTemplate::New(set48hzV8)->GetFunction());

    tpl->PrototypeTemplate()->Set(v8::String::NewSymbol("set188hz"),
        FunctionTemplate::New(set188hzV8)->GetFunction());

    constructor = Persistent<Function>::New(tpl->GetFunction());
    exports->Set(v8::String::NewSymbol("Servo"), constructor);
}
static void SetMemberFunc(Handle<Object> obj) {}

static void SetConst(Handle<Object> obj) {

    obj->Set(v8::String::NewSymbol("MIN_ANGLE"),
             Int32::New(0));

    obj->Set(v8::String::NewSymbol("MAX_ANGLE"),
             Int32::New(180));

    obj->Set(v8::String::NewSymbol("MIN_PULSE_WIDTH"),
             Int32::New(544));

    obj->Set(v8::String::NewSymbol("MAX_PULSE_WIDTH"),
             Int32::New(2000));

    obj->Set(v8::String::NewSymbol("DEFAULT_PULSE_WIDTH"),
             Int32::New(1500));

    obj->Set(v8::String::NewSymbol("INVALID_SERVO"),
             Int32::New(255));

    obj->Set(v8::String::NewSymbol("GPORT0_BIT4_PWM7"),
             Int32::New(0x10));

    obj->Set(v8::String::NewSymbol("GPORT0_BIT1_PWM5"),
             Int32::New(0x02));

    obj->Set(v8::String::NewSymbol("GPORT1_BIT0_PWM6"),
             Int32::New(0xff));

    obj->Set(v8::String::NewSymbol("GPORT0_BIT3_PWM1"),
             Int32::New(0x08));

    obj->Set(v8::String::NewSymbol("GPORT0_BIT0_PWM7"),
             Int32::New(0x01));

    obj->Set(v8::String::NewSymbol("GPORT1_BIT1_PWM4"),
             Int32::New(0xff));

    obj->Set(v8::String::NewSymbol("CYPRESS_I2C_ADDRESS"),
             Int32::New(0x20));

    obj->Set(v8::String::NewSymbol("MAX_NUMBER_OF_SERVOS"),
             Int32::New(6));

    obj->Set(v8::String::NewSymbol("MY_TRACE_PREFIX"),
             v8::String::New("ServoX86Lib"));

}
void InitServo(Handle<Object> exports) {

    ServoV8::Init(exports);

    SetMemberFunc(exports);

    SetConst(exports);
}
