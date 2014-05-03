#include "version_export_addon.h"

// 1: extern char * version_addon ( ) ;
Handle<Value> version_addonV8(const Arguments &args) {
    HandleScope scope;
        
    char* ret = version_addon();
    
    return scope.Close(v8::String::New((char*)ret));
}
static void SetMemberFunc(Handle<Object> obj) {
    obj->Set(v8::String::NewSymbol("version_addon"),
           FunctionTemplate::New(version_addonV8)->GetFunction());
}

static void SetConst(Handle<Object> obj) {

}
void Initversion_export(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);
}
