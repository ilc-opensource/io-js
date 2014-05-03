#include "sysfs_addon.h"

// 8: int sysfsPwmExport ( unsigned pwm , int * handle_enable , int * handle_duty ) ;
// Can not be transfered!

// 9: int sysfsPwmEnable ( int handle_enable , int handle_duty , unsigned int ulValue ) ;
Handle<Value> sysfsPwmEnableV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32() && args[1]->IsInt32() && args[2]->IsUint32(), "parameters error!");
    
    int arg0 = (int)args[0]->IntegerValue();
    int arg1 = (int)args[1]->IntegerValue();
    unsigned int arg2 = (unsigned int)args[2]->Uint32Value();
        
    int ret = sysfsPwmEnable(arg0, arg1, arg2);
    
    return scope.Close(Int32::New((int)ret));
}
// 10: int sysfsPwmDisable ( int handle_enable ) ;
Handle<Value> sysfsPwmDisableV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32(), "parameters error!");
    
    int arg0 = (int)args[0]->IntegerValue();
        
    int ret = sysfsPwmDisable(arg0);
    
    return scope.Close(Int32::New((int)ret));
}
// 12: int sysfsGpioSet ( int ihandle , unsigned int value ) ;
Handle<Value> sysfsGpioSetV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32() && args[1]->IsUint32(), "parameters error!");
    
    int arg0 = (int)args[0]->IntegerValue();
    unsigned int arg1 = (unsigned int)args[1]->Uint32Value();
        
    int ret = sysfsGpioSet(arg0, arg1);
    
    return scope.Close(Int32::New((int)ret));
}
// 13: int sysfsGpioGet ( int ihandle ) ;
Handle<Value> sysfsGpioGetV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32(), "parameters error!");
    
    int arg0 = (int)args[0]->IntegerValue();
        
    int ret = sysfsGpioGet(arg0);
    
    return scope.Close(Int32::New((int)ret));
}
// 14: int sysfsGpioExport ( unsigned int gpio , char * path , unsigned int max_path ) ;
Handle<Value> sysfsGpioExportV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsString() && args[2]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    v8::String::AsciiValue arg1Str(args[1]->ToString());
    char * arg1 = (char *)*arg1Str;
    unsigned int arg2 = (unsigned int)args[2]->Uint32Value();
        
    int ret = sysfsGpioExport(arg0, arg1, arg2);
    
    return scope.Close(Int32::New((int)ret));
}
// 15: int sysfsGpioDirection ( unsigned int gpio , int output , int outval ) ;
Handle<Value> sysfsGpioDirectionV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsInt32() && args[2]->IsInt32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    int arg1 = (int)args[1]->IntegerValue();
    int arg2 = (int)args[2]->IntegerValue();
        
    int ret = sysfsGpioDirection(arg0, arg1, arg2);
    
    return scope.Close(Int32::New((int)ret));
}
// 16: int sysfsGpioEdgeConfig ( unsigned int gpio , int mode ) ;
Handle<Value> sysfsGpioEdgeConfigV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsInt32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    int arg1 = (int)args[1]->IntegerValue();
        
    int ret = sysfsGpioEdgeConfig(arg0, arg1);
    
    return scope.Close(Int32::New((int)ret));
}
// 17: int sysfsGpioLevelConfig ( unsigned int gpio , int mode ) ;
Handle<Value> sysfsGpioLevelConfigV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsInt32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    int arg1 = (int)args[1]->IntegerValue();
        
    int ret = sysfsGpioLevelConfig(arg0, arg1);
    
    return scope.Close(Int32::New((int)ret));
}
// 18: int sysfsGpioSetDrive ( unsigned int gpio , unsigned int mode ) ;
Handle<Value> sysfsGpioSetDriveV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    unsigned int arg1 = (unsigned int)args[1]->Uint32Value();
        
    int ret = sysfsGpioSetDrive(arg0, arg1);
    
    return scope.Close(Int32::New((int)ret));
}
static void SetMemberFunc(Handle<Object> obj) {
    obj->Set(v8::String::NewSymbol("sysfsPwmEnable"),
           FunctionTemplate::New(sysfsPwmEnableV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("sysfsPwmDisable"),
           FunctionTemplate::New(sysfsPwmDisableV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("sysfsGpioSet"),
           FunctionTemplate::New(sysfsGpioSetV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("sysfsGpioGet"),
           FunctionTemplate::New(sysfsGpioGetV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("sysfsGpioExport"),
           FunctionTemplate::New(sysfsGpioExportV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("sysfsGpioDirection"),
           FunctionTemplate::New(sysfsGpioDirectionV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("sysfsGpioEdgeConfig"),
           FunctionTemplate::New(sysfsGpioEdgeConfigV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("sysfsGpioLevelConfig"),
           FunctionTemplate::New(sysfsGpioLevelConfigV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("sysfsGpioSetDrive"),
           FunctionTemplate::New(sysfsGpioSetDriveV8)->GetFunction());
}

static void SetConst(Handle<Object> obj) {

}
void Initsysfs(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);
}
