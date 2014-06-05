#include "sysfs_addon.h"
#include "stdlib.h"
#include "string.h"
#include "_callback.h"

// 8: int sysfsPwmExport ( unsigned pwm , int * handle_enable , int * handle_duty ) ;
Handle<Value> sysfsPwmExportV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsArray() && args[2]->IsArray(), "parameters error!");
    
    // Convert V8 parameters to C++
    unsigned arg0 = (unsigned)args[0]->Uint32Value();
    
    int index1;
    Local<Array> argV8_1 = Local<Array>::Cast(args[1]);
    int len1 = argV8_1->Length();
    int arg1[len1];
    for (index1 = 0; index1 < (int)argV8_1->Length(); index1++) {
      Local<Value> argV8_1_index1 = argV8_1->Get(index1);
      V8_ASSERT(argV8_1_index1->IsInt32(), "arg1[%d] parameter error", index1);
      arg1[index1] = (int)argV8_1_index1->IntegerValue();
    }
    int index2;
    Local<Array> argV8_2 = Local<Array>::Cast(args[2]);
    int len2 = argV8_2->Length();
    int arg2[len2];
    for (index2 = 0; index2 < (int)argV8_2->Length(); index2++) {
      Local<Value> argV8_2_index2 = argV8_2->Get(index2);
      V8_ASSERT(argV8_2_index2->IsInt32(), "arg2[%d] parameter error", index2);
      arg2[index2] = (int)argV8_2_index2->IntegerValue();
    }
        
    // Call C++ function
    int ret = sysfsPwmExport(arg0, arg1, arg2);
    
    // Convert C++ parameters passed by pointer to V8
    for (index1 = 0; index1 < len1; index1 ++)
      argV8_1->Set(index1, Int32::New((int)arg1[index1]));
    for (index2 = 0; index2 < len2; index2 ++)
      argV8_2->Set(index2, Int32::New((int)arg2[index2]));
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 9: int sysfsPwmEnable ( int handle_enable , int handle_duty , unsigned int ulValue ) ;
Handle<Value> sysfsPwmEnableV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32() && args[1]->IsInt32() && args[2]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    int arg0 = (int)args[0]->IntegerValue();
    
    int arg1 = (int)args[1]->IntegerValue();
    
    unsigned int arg2 = (unsigned int)args[2]->Uint32Value();
    
        
    // Call C++ function
    int ret = sysfsPwmEnable(arg0, arg1, arg2);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 10: int sysfsPwmDisable ( int handle_enable ) ;
Handle<Value> sysfsPwmDisableV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32(), "parameters error!");
    
    // Convert V8 parameters to C++
    int arg0 = (int)args[0]->IntegerValue();
    
        
    // Call C++ function
    int ret = sysfsPwmDisable(arg0);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 12: int sysfsGpioSet ( int ihandle , unsigned int value ) ;
Handle<Value> sysfsGpioSetV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32() && args[1]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    int arg0 = (int)args[0]->IntegerValue();
    
    unsigned int arg1 = (unsigned int)args[1]->Uint32Value();
    
        
    // Call C++ function
    int ret = sysfsGpioSet(arg0, arg1);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 13: int sysfsGpioGet ( int ihandle ) ;
Handle<Value> sysfsGpioGetV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32(), "parameters error!");
    
    // Convert V8 parameters to C++
    int arg0 = (int)args[0]->IntegerValue();
    
        
    // Call C++ function
    int ret = sysfsGpioGet(arg0);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 14: int sysfsGpioExport ( unsigned int gpio , char * path , unsigned int max_path ) ;
Handle<Value> sysfsGpioExportV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && (args[1]->IsString() || args[1]->IsObject()) && args[2]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    
    char *arg1;
    int index1;
    int len1;
    if (args[1]->IsString()) {
        String::AsciiValue argV8_1(args[1]->ToString());
        len1 = strlen(*argV8_1) + 1;
        arg1 = (char *)malloc(len1 * sizeof(char));
        strcpy(arg1, *argV8_1);
    } else {
        Local<Array> argV8_1 = Local<Array>::Cast(args[1]);
        len1 = argV8_1->Length() + 1;
        arg1 = (char *)malloc(len1 * sizeof(char));
        for (index1 = 0; index1 < len1 - 1; index1++) {
            Local<Value> argV8_1_index1 = argV8_1->Get(index1);
            V8_ASSERT(argV8_1_index1->IsInt32(), "arg1[%d] parameter error", index1);
            arg1[index1] = (char)argV8_1_index1->IntegerValue();
        }
        arg1[index1] = 0;
    }
    unsigned int arg2 = (unsigned int)args[2]->Uint32Value();
    
        
    // Call C++ function
    int ret = sysfsGpioExport(arg0, arg1, arg2);
    
    // Convert C++ parameters passed by pointer to V8
    
    if (args[1]->IsString()) {
        String::AsciiValue argV8_1(args[1]->ToString());
        const char *oldStr = *argV8_1;
        for (index1 = 0; index1 < len1; index1++) {
            if (oldStr[index1] != arg1[index1])
                V8_ASSERT(false, "String arg1 is Changed in C function, \
    Please Use Buffer or Integer Array to map 'char *' in JS");
        }
    } else {
        Local<Array> argV8_1 = Local<Array>::Cast(args[1]);
        for (index1 = 0; index1 < len1; index1++) {
            argV8_1->Set(index1, Int32::New((int)arg1[index1]));
        }
    }
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 15: int sysfsGpioDirection ( unsigned int gpio , int output , int outval ) ;
Handle<Value> sysfsGpioDirectionV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsInt32() && args[2]->IsInt32(), "parameters error!");
    
    // Convert V8 parameters to C++
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    
    int arg1 = (int)args[1]->IntegerValue();
    
    int arg2 = (int)args[2]->IntegerValue();
    
        
    // Call C++ function
    int ret = sysfsGpioDirection(arg0, arg1, arg2);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 16: int sysfsGpioEdgeConfig ( unsigned int gpio , int mode ) ;
Handle<Value> sysfsGpioEdgeConfigV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsInt32(), "parameters error!");
    
    // Convert V8 parameters to C++
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    
    int arg1 = (int)args[1]->IntegerValue();
    
        
    // Call C++ function
    int ret = sysfsGpioEdgeConfig(arg0, arg1);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 17: int sysfsGpioLevelConfig ( unsigned int gpio , int mode ) ;
Handle<Value> sysfsGpioLevelConfigV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsInt32(), "parameters error!");
    
    // Convert V8 parameters to C++
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    
    int arg1 = (int)args[1]->IntegerValue();
    
        
    // Call C++ function
    int ret = sysfsGpioLevelConfig(arg0, arg1);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 18: int sysfsGpioSetDrive ( unsigned int gpio , unsigned int mode ) ;
Handle<Value> sysfsGpioSetDriveV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    
    unsigned int arg1 = (unsigned int)args[1]->Uint32Value();
    
        
    // Call C++ function
    int ret = sysfsGpioSetDrive(arg0, arg1);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
static void SetMemberFunc(Handle<Object> obj) {
    obj->Set(v8::String::NewSymbol("sysfsPwmExport"),
           FunctionTemplate::New(sysfsPwmExportV8)->GetFunction());

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


// Const defined by macros
static void SetConst(Handle<Object> obj) {

}

// Const defined by enumeration
static void SetEnumConst(Handle<Object> obj) {

}
static void SetGlobalVarFunc(Handle<Object> obj) {
}

void Initsysfs(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);

    SetEnumConst(exports);

    SetGlobalVarFunc(exports);
}
