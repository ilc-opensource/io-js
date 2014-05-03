#include "Arduino_addon.h"

static void SetMemberFunc(Handle<Object> obj) {}

static void SetConst(Handle<Object> obj) {

    obj->Set(v8::String::NewSymbol("INPUT"),
             Int32::New(0x00));

    obj->Set(v8::String::NewSymbol("OUTPUT"),
             Int32::New(0x01));

    obj->Set(v8::String::NewSymbol("INPUT_PULLUP"),
             Int32::New(0x02));

    obj->Set(v8::String::NewSymbol("OUTPUT_FAST"),
             Int32::New(0x03));

    obj->Set(v8::String::NewSymbol("INPUT_FAST"),
             Int32::New(0x04));

    obj->Set(v8::String::NewSymbol("DEFAULT"),
             Int32::New(0));

    obj->Set(v8::String::NewSymbol("true"),
             Int32::New(0x1));

    obj->Set(v8::String::NewSymbol("false"),
             Int32::New(0x0));

    obj->Set(v8::String::NewSymbol("DEG_TO_RAD"),
             Number::New(0.017453292519943295769236907684886));

    obj->Set(v8::String::NewSymbol("RAD_TO_DEG"),
             Number::New(57.295779513082320876798154814105));

    obj->Set(v8::String::NewSymbol("SERIAL"),
             Int32::New(0x0));

    obj->Set(v8::String::NewSymbol("DISPLAY"),
             Int32::New(0x1));

    obj->Set(v8::String::NewSymbol("LSBFIRST"),
             Int32::New(0));

    obj->Set(v8::String::NewSymbol("MSBFIRST"),
             Int32::New(1));

    obj->Set(v8::String::NewSymbol("PA"),
             Int32::New(1));

    obj->Set(v8::String::NewSymbol("PB"),
             Int32::New(2));

    obj->Set(v8::String::NewSymbol("PC"),
             Int32::New(3));

    obj->Set(v8::String::NewSymbol("PD"),
             Int32::New(4));

    obj->Set(v8::String::NewSymbol("PE"),
             Int32::New(5));

    obj->Set(v8::String::NewSymbol("PF"),
             Int32::New(6));

    obj->Set(v8::String::NewSymbol("PG"),
             Int32::New(7));

    obj->Set(v8::String::NewSymbol("PH"),
             Int32::New(8));

    obj->Set(v8::String::NewSymbol("PJ"),
             Int32::New(10));

    obj->Set(v8::String::NewSymbol("PK"),
             Int32::New(11));

    obj->Set(v8::String::NewSymbol("PL"),
             Int32::New(12));

}
void InitArduino(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);
}
