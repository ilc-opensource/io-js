#include "OSAbstract_norm_addon.h"

// 6: void initWithTty ( char * tty0 , char * tty1 , char * tty2 ) ;
Handle<Value> initWithTtyV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsString() && args[1]->IsString() && args[2]->IsString(), "parameters error!");
    
    v8::String::AsciiValue arg0Str(args[0]->ToString());
    char * arg0 = (char *)*arg0Str;
    v8::String::AsciiValue arg1Str(args[1]->ToString());
    char * arg1 = (char *)*arg1Str;
    v8::String::AsciiValue arg2Str(args[2]->ToString());
    char * arg2 = (char *)*arg2Str;
        
    initWithTty(arg0, arg1, arg2);
    
    return scope.Close(Undefined());
    
}
static void SetMemberFunc(Handle<Object> obj) {
    obj->Set(v8::String::NewSymbol("initWithTty"),
           FunctionTemplate::New(initWithTtyV8)->GetFunction());
}

static void SetConst(Handle<Object> obj) {

}
void InitOSAbstract_norm(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);
}
