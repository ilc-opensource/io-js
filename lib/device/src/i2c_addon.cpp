#include "i2c_addon.h"

// 30: int i2c_getadapter ( uint32_t i2c_bus_address ) ;
Handle<Value> i2c_getadapterV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
        
    int ret = i2c_getadapter(arg0);
    
    return scope.Close(Int32::New((int)ret));
}
// 31: int i2c_openadapter ( uint8_t i2c_adapter_nr ) ;
Handle<Value> i2c_openadapterV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
        
    int ret = i2c_openadapter(arg0);
    
    return scope.Close(Int32::New((int)ret));
}
// 32: int i2c_setslave ( int i2c_fd , uint8_t addr ) ;
Handle<Value> i2c_setslaveV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32() && args[1]->IsUint32(), "parameters error!");
    
    int arg0 = (int)args[0]->IntegerValue();
    unsigned int arg1 = (unsigned int)args[1]->Uint32Value();
        
    int ret = i2c_setslave(arg0, arg1);
    
    return scope.Close(Int32::New((int)ret));
}
// 33: int i2c_writebyte ( int i2c_fd , uint8_t byte ) ;
Handle<Value> i2c_writebyteV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32() && args[1]->IsUint32(), "parameters error!");
    
    int arg0 = (int)args[0]->IntegerValue();
    unsigned int arg1 = (unsigned int)args[1]->Uint32Value();
        
    int ret = i2c_writebyte(arg0, arg1);
    
    return scope.Close(Int32::New((int)ret));
}
// 34: int i2c_writebytes ( int i2c_fd , uint8_t * bytes , uint8_t length ) ;
Handle<Value> i2c_writebytesV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32() && args[1]->IsString() && args[2]->IsUint32(), "parameters error!");
    
    int arg0 = (int)args[0]->IntegerValue();
    v8::String::AsciiValue arg1Str(args[1]->ToString());
    uint8_t * arg1 = (uint8_t *)*arg1Str;
    unsigned int arg2 = (unsigned int)args[2]->Uint32Value();
        
    int ret = i2c_writebytes(arg0, arg1, arg2);
    
    return scope.Close(Int32::New((int)ret));
}
// 35: int i2c_readbyte ( int i2c_fd ) ;
Handle<Value> i2c_readbyteV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32(), "parameters error!");
    
    int arg0 = (int)args[0]->IntegerValue();
        
    int ret = i2c_readbyte(arg0);
    
    return scope.Close(Int32::New((int)ret));
}
// 36: int i2c_readbytes ( int i2c_fd , uint8_t * buf , int length ) ;
Handle<Value> i2c_readbytesV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32() && args[1]->IsString() && args[2]->IsInt32(), "parameters error!");
    
    int arg0 = (int)args[0]->IntegerValue();
    v8::String::AsciiValue arg1Str(args[1]->ToString());
    uint8_t * arg1 = (uint8_t *)*arg1Str;
    int arg2 = (int)args[2]->IntegerValue();
        
    int ret = i2c_readbytes(arg0, arg1, arg2);
    
    return scope.Close(Int32::New((int)ret));
}
// 37: int i2c_readwrite ( int i2c_fd ) ;
Handle<Value> i2c_readwriteV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32(), "parameters error!");
    
    int arg0 = (int)args[0]->IntegerValue();
        
    int ret = i2c_readwrite(arg0);
    
    return scope.Close(Int32::New((int)ret));
}
// 38: int i2c_add_to_buf ( uint8_t addr , uint8_t rw , uint8_t * value , int length ) ;
Handle<Value> i2c_add_to_bufV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsUint32() && args[2]->IsString() && args[3]->IsInt32(), "parameters error!");
    
    unsigned int arg0 = (unsigned int)args[0]->Uint32Value();
    unsigned int arg1 = (unsigned int)args[1]->Uint32Value();
    v8::String::AsciiValue arg2Str(args[2]->ToString());
    uint8_t * arg2 = (uint8_t *)*arg2Str;
    int arg3 = (int)args[3]->IntegerValue();
        
    int ret = i2c_add_to_buf(arg0, arg1, arg2, arg3);
    
    return scope.Close(Int32::New((int)ret));
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

static void SetConst(Handle<Object> obj) {

}
void Initi2c(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);
}
