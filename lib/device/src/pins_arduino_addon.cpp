#include "pins_arduino_addon.h"

static void SetMemberFunc(Handle<Object> obj) {}

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
void Initpins_arduino(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);
}
