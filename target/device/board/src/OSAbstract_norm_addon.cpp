#include "OSAbstract_norm_addon.h"
#include "stdlib.h"
#include "string.h"
#include "_callback.h"

// 6: void initWithTty ( char * tty0 , char * tty1 , char * tty2 ) ;
Handle<Value> initWithTtyV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT((args[0]->IsString() || args[0]->IsObject()) && (args[1]->IsString() || args[1]->IsObject()) && (args[2]->IsString() || args[2]->IsObject()), "parameters error!");
    
    // Convert V8 parameters to C++
    char *arg0;
    int index0;
    int len0;
    if (args[0]->IsString()) {
        String::AsciiValue argV8_0(args[0]->ToString());
        len0 = strlen(*argV8_0) + 1;
        arg0 = (char *)malloc(len0 * sizeof(char));
        strcpy(arg0, *argV8_0);
    } else {
        Local<Array> argV8_0 = Local<Array>::Cast(args[0]);
        len0 = argV8_0->Length() + 1;
        arg0 = (char *)malloc(len0 * sizeof(char));
        for (index0 = 0; index0 < len0 - 1; index0++) {
            Local<Value> argV8_0_index0 = argV8_0->Get(index0);
            V8_ASSERT(argV8_0_index0->IsInt32(), "arg0[%d] parameter error", index0);
            arg0[index0] = (char)argV8_0_index0->IntegerValue();
        }
        arg0[index0] = 0;
    }
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
    char *arg2;
    int index2;
    int len2;
    if (args[2]->IsString()) {
        String::AsciiValue argV8_2(args[2]->ToString());
        len2 = strlen(*argV8_2) + 1;
        arg2 = (char *)malloc(len2 * sizeof(char));
        strcpy(arg2, *argV8_2);
    } else {
        Local<Array> argV8_2 = Local<Array>::Cast(args[2]);
        len2 = argV8_2->Length() + 1;
        arg2 = (char *)malloc(len2 * sizeof(char));
        for (index2 = 0; index2 < len2 - 1; index2++) {
            Local<Value> argV8_2_index2 = argV8_2->Get(index2);
            V8_ASSERT(argV8_2_index2->IsInt32(), "arg2[%d] parameter error", index2);
            arg2[index2] = (char)argV8_2_index2->IntegerValue();
        }
        arg2[index2] = 0;
    }
        
    // Call C++ function
    initWithTty(arg0, arg1, arg2);
    
    // Convert C++ parameters passed by pointer to V8
    
    if (args[0]->IsString()) {
        String::AsciiValue argV8_0(args[0]->ToString());
        const char *oldStr = *argV8_0;
        for (index0 = 0; index0 < len0; index0++) {
            if (oldStr[index0] != arg0[index0])
                V8_ASSERT(false, "String arg0 is Changed in C function, \
    Please Use Buffer or Integer Array to map 'char *' in JS");
        }
    } else {
        Local<Array> argV8_0 = Local<Array>::Cast(args[0]);
        for (index0 = 0; index0 < len0; index0++) {
            argV8_0->Set(index0, Int32::New((int)arg0[index0]));
        }
    }
    
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
    
    if (args[2]->IsString()) {
        String::AsciiValue argV8_2(args[2]->ToString());
        const char *oldStr = *argV8_2;
        for (index2 = 0; index2 < len2; index2++) {
            if (oldStr[index2] != arg2[index2])
                V8_ASSERT(false, "String arg2 is Changed in C function, \
    Please Use Buffer or Integer Array to map 'char *' in JS");
        }
    } else {
        Local<Array> argV8_2 = Local<Array>::Cast(args[2]);
        for (index2 = 0; index2 < len2; index2++) {
            argV8_2->Set(index2, Int32::New((int)arg2[index2]));
        }
    }
    
    return scope.Close(Undefined());
    
}
static void SetMemberFunc(Handle<Object> obj) {
    obj->Set(v8::String::NewSymbol("initWithTty"),
           FunctionTemplate::New(initWithTtyV8)->GetFunction());
}


// Const defined by macros
static void SetConst(Handle<Object> obj) {

}

// Const defined by enumeration
static void SetEnumConst(Handle<Object> obj) {

}
static void SetGlobalVarFunc(Handle<Object> obj) {
}

void InitOSAbstract_norm(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);

    SetEnumConst(exports);

    SetGlobalVarFunc(exports);
}
