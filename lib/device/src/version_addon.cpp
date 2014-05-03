#include "version_addon.h"

// 1: extern char * version ( ) ;
Handle<Value> versionV8(const Arguments &args) {
    HandleScope scope;
        
    char* ret = version();
    
    return scope.Close(v8::String::New((char*)ret));
}
static void SetMemberFunc(Handle<Object> obj) {
    obj->Set(v8::String::NewSymbol("version"),
           FunctionTemplate::New(versionV8)->GetFunction());
}

static void SetConst(Handle<Object> obj) {

}
void Initversion(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);
}
