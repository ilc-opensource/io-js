#include "i2c_addon.h"
#include "stdlib.h"
#include "string.h"
#include "_callback.h"

// 30: int i2c_getadapter ( uint32_t i2c_bus_address ) ;
Handle<Value> i2c_getadapterV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint32_t arg0 = (uint32_t)args[0]->Uint32Value();
    
        
    // Call C++ function
    int ret = i2c_getadapter(arg0);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 31: int i2c_openadapter ( uint8_t i2c_adapter_nr ) ;
Handle<Value> i2c_openadapterV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
        
    // Call C++ function
    int ret = i2c_openadapter(arg0);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 32: int i2c_setslave ( int i2c_fd , uint8_t addr ) ;
Handle<Value> i2c_setslaveV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32() && args[1]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    int arg0 = (int)args[0]->IntegerValue();
    
    uint8_t arg1 = (uint8_t)args[1]->Uint32Value();
    
        
    // Call C++ function
    int ret = i2c_setslave(arg0, arg1);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 33: int i2c_writebyte ( int i2c_fd , uint8_t byte ) ;
Handle<Value> i2c_writebyteV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32() && args[1]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    int arg0 = (int)args[0]->IntegerValue();
    
    uint8_t arg1 = (uint8_t)args[1]->Uint32Value();
    
        
    // Call C++ function
    int ret = i2c_writebyte(arg0, arg1);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 34: int i2c_writebytes ( int i2c_fd , uint8_t * bytes , uint8_t length ) ;
Handle<Value> i2c_writebytesV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32() && (args[1]->IsString() || args[1]->IsObject()) && args[2]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    int arg0 = (int)args[0]->IntegerValue();
    
    int index1;
    Local<Array> argV8_1 = Local<Array>::Cast(args[1]);
    int len1 = argV8_1->Length();
    uint8_t arg1[len1];
    for (index1 = 0; index1 < (int)argV8_1->Length(); index1++) {
      Local<Value> argV8_1_index1 = argV8_1->Get(index1);
      V8_ASSERT(argV8_1_index1->IsUint32(), "arg1[%d] parameter error", index1);
      arg1[index1] = (uint8_t)argV8_1_index1->Uint32Value();
    }
    uint8_t arg2 = (uint8_t)args[2]->Uint32Value();
    
        
    // Call C++ function
    int ret = i2c_writebytes(arg0, arg1, arg2);
    
    // Convert C++ parameters passed by pointer to V8
    for (index1 = 0; index1 < len1; index1 ++)
      argV8_1->Set(index1, Uint32::New((unsigned int)arg1[index1]));
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 35: int i2c_readbyte ( int i2c_fd ) ;
Handle<Value> i2c_readbyteV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32(), "parameters error!");
    
    // Convert V8 parameters to C++
    int arg0 = (int)args[0]->IntegerValue();
    
        
    // Call C++ function
    int ret = i2c_readbyte(arg0);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 36: int i2c_readbytes ( int i2c_fd , uint8_t * buf , int length ) ;
Handle<Value> i2c_readbytesV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32() && (args[1]->IsString() || args[1]->IsObject()) && args[2]->IsInt32(), "parameters error!");
    
    // Convert V8 parameters to C++
    int arg0 = (int)args[0]->IntegerValue();
    
    int index1;
    Local<Array> argV8_1 = Local<Array>::Cast(args[1]);
    int len1 = argV8_1->Length();
    uint8_t arg1[len1];
    for (index1 = 0; index1 < (int)argV8_1->Length(); index1++) {
      Local<Value> argV8_1_index1 = argV8_1->Get(index1);
      V8_ASSERT(argV8_1_index1->IsUint32(), "arg1[%d] parameter error", index1);
      arg1[index1] = (uint8_t)argV8_1_index1->Uint32Value();
    }
    int arg2 = (int)args[2]->IntegerValue();
    
        
    // Call C++ function
    int ret = i2c_readbytes(arg0, arg1, arg2);
    
    // Convert C++ parameters passed by pointer to V8
    for (index1 = 0; index1 < len1; index1 ++)
      argV8_1->Set(index1, Uint32::New((unsigned int)arg1[index1]));
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 37: int i2c_readwrite ( int i2c_fd ) ;
Handle<Value> i2c_readwriteV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32(), "parameters error!");
    
    // Convert V8 parameters to C++
    int arg0 = (int)args[0]->IntegerValue();
    
        
    // Call C++ function
    int ret = i2c_readwrite(arg0);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 38: int i2c_add_to_buf ( uint8_t addr , uint8_t rw , uint8_t * value , int length ) ;
Handle<Value> i2c_add_to_bufV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsUint32() && (args[2]->IsString() || args[2]->IsObject()) && args[3]->IsInt32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
    uint8_t arg1 = (uint8_t)args[1]->Uint32Value();
    
    int index2;
    Local<Array> argV8_2 = Local<Array>::Cast(args[2]);
    int len2 = argV8_2->Length();
    uint8_t arg2[len2];
    for (index2 = 0; index2 < (int)argV8_2->Length(); index2++) {
      Local<Value> argV8_2_index2 = argV8_2->Get(index2);
      V8_ASSERT(argV8_2_index2->IsUint32(), "arg2[%d] parameter error", index2);
      arg2[index2] = (uint8_t)argV8_2_index2->Uint32Value();
    }
    int arg3 = (int)args[3]->IntegerValue();
    
        
    // Call C++ function
    int ret = i2c_add_to_buf(arg0, arg1, arg2, arg3);
    
    // Convert C++ parameters passed by pointer to V8
    for (index2 = 0; index2 < len2; index2 ++)
      argV8_2->Set(index2, Uint32::New((unsigned int)arg2[index2]));
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
static void SetMemberFunc(Handle<Object> obj) {
    obj->Set(v8::String::NewSymbol("i2c_getadapter"),
           FunctionTemplate::New(i2c_getadapterV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("i2c_openadapter"),
           FunctionTemplate::New(i2c_openadapterV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("i2c_setslave"),
           FunctionTemplate::New(i2c_setslaveV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("i2c_writebyte"),
           FunctionTemplate::New(i2c_writebyteV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("i2c_writebytes"),
           FunctionTemplate::New(i2c_writebytesV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("i2c_readbyte"),
           FunctionTemplate::New(i2c_readbyteV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("i2c_readbytes"),
           FunctionTemplate::New(i2c_readbytesV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("i2c_readwrite"),
           FunctionTemplate::New(i2c_readwriteV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("i2c_add_to_buf"),
           FunctionTemplate::New(i2c_add_to_bufV8)->GetFunction());
}


// Const defined by macros
static void SetConst(Handle<Object> obj) {

}

// Const defined by enumeration
static void SetEnumConst(Handle<Object> obj) {

}
static void SetGlobalVarFunc(Handle<Object> obj) {
}

void Initi2c(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);

    SetEnumConst(exports);

    SetGlobalVarFunc(exports);
}
