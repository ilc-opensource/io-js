#include "pin_map_norm_addon.h"
#include "stdlib.h"
#include "string.h"
#include "_callback.h"

static void SetMemberFunc(Handle<Object> obj) {}


// Const defined by macros
static void SetConst(Handle<Object> obj) {

    obj->Set(v8::String::NewSymbol("A0"),
             Int32::New(0xE));

    obj->Set(v8::String::NewSymbol("A1"),
             Int32::New(0xF));

    obj->Set(v8::String::NewSymbol("A2"),
             Int32::New(0x10));

    obj->Set(v8::String::NewSymbol("A3"),
             Int32::New(0x11));

    obj->Set(v8::String::NewSymbol("A4"),
             Int32::New(0x12));

    obj->Set(v8::String::NewSymbol("A5"),
             Int32::New(0x13));

    obj->Set(v8::String::NewSymbol("A6"),
             Int32::New(0x14));

    obj->Set(v8::String::NewSymbol("A7"),
             Int32::New(0x15));

}

// Const defined by enumeration
static void SetEnumConst(Handle<Object> obj) {

}
static void SetGlobalVarFunc(Handle<Object> obj) {
}

void Initpin_map_norm(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);

    SetEnumConst(exports);

    SetGlobalVarFunc(exports);
}
