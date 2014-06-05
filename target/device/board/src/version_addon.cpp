#include "version_addon.h"
#include "stdlib.h"
#include "string.h"
#include "_callback.h"

// 1: extern char * version ( ) ;
Handle<Value> versionV8(const Arguments &args) {
    HandleScope scope;
        
    // Call C++ function
    char* ret = version();
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = v8::String::New((char*)ret);
    
    return scope.Close(retV8);
}
static void SetMemberFunc(Handle<Object> obj) {
    obj->Set(v8::String::NewSymbol("version"),
           FunctionTemplate::New(versionV8)->GetFunction());
}


// Const defined by macros
static void SetConst(Handle<Object> obj) {

}

// Const defined by enumeration
static void SetEnumConst(Handle<Object> obj) {

}
static void SetGlobalVarFunc(Handle<Object> obj) {
}

void Initversion(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);

    SetEnumConst(exports);

    SetGlobalVarFunc(exports);
}
