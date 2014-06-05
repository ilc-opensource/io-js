#include "variant_norm_addon.h"
#include "stdlib.h"
#include "string.h"
#include "_callback.h"

// 46: int muxSelectDigitalPin ( uint8_t pin ) ;
Handle<Value> muxSelectDigitalPinV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
        
    // Call C++ function
    int ret = muxSelectDigitalPin(arg0);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 47: int muxSelectAnalogPin ( uint8_t pin ) ;
Handle<Value> muxSelectAnalogPinV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
        
    // Call C++ function
    int ret = muxSelectAnalogPin(arg0);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 48: int muxSelectUart ( uint8_t interface ) ;
Handle<Value> muxSelectUartV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
        
    // Call C++ function
    int ret = muxSelectUart(arg0);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 49: int muxSelectSpi ( uint8_t interface ) ;
Handle<Value> muxSelectSpiV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
        
    // Call C++ function
    int ret = muxSelectSpi(arg0);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 50: int muxSelectI2c ( uint8_t interface ) ;
Handle<Value> muxSelectI2cV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
        
    // Call C++ function
    int ret = muxSelectI2c(arg0);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 55: int variantPinMode ( uint8_t pin , uint8_t mode ) ;
Handle<Value> variantPinModeV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
    uint8_t arg1 = (uint8_t)args[1]->Uint32Value();
    
        
    // Call C++ function
    int ret = variantPinMode(arg0, arg1);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 56: int variantPinModeIRQ ( uint8_t pin , uint8_t mode ) ;
Handle<Value> variantPinModeIRQV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
    uint8_t arg1 = (uint8_t)args[1]->Uint32Value();
    
        
    // Call C++ function
    int ret = variantPinModeIRQ(arg0, arg1);
    
    // Convert C++ return value to V8
    Handle<Value> retV8 = Int32::New((int)ret);
    
    return scope.Close(retV8);
}
// 57: void turnOffPWM ( uint8_t pin ) ;
Handle<Value> turnOffPWMV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
        
    // Call C++ function
    turnOffPWM(arg0);
    
    return scope.Close(Undefined());
    
}
// 58: void turnOnPWM ( uint8_t pin ) ;
Handle<Value> turnOnPWMV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
        
    // Call C++ function
    turnOnPWM(arg0);
    
    return scope.Close(Undefined());
    
}
// 60: void variantEnableFastGpio ( int pin ) ;
Handle<Value> variantEnableFastGpioV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsInt32(), "parameters error!");
    
    // Convert V8 parameters to C++
    int arg0 = (int)args[0]->IntegerValue();
    
        
    // Call C++ function
    variantEnableFastGpio(arg0);
    
    return scope.Close(Undefined());
    
}
// 62: void variantEnablePullup ( uint8_t pin , int enable ) ;
Handle<Value> variantEnablePullupV8(const Arguments &args) {
    HandleScope scope;
    
    V8_ASSERT(args[0]->IsUint32() && args[1]->IsInt32(), "parameters error!");
    
    // Convert V8 parameters to C++
    uint8_t arg0 = (uint8_t)args[0]->Uint32Value();
    
    int arg1 = (int)args[1]->IntegerValue();
    
        
    // Call C++ function
    variantEnablePullup(arg0, arg1);
    
    return scope.Close(Undefined());
    
}
static void SetMemberFunc(Handle<Object> obj) {
    obj->Set(v8::String::NewSymbol("muxSelectDigitalPin"),
           FunctionTemplate::New(muxSelectDigitalPinV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("muxSelectAnalogPin"),
           FunctionTemplate::New(muxSelectAnalogPinV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("muxSelectUart"),
           FunctionTemplate::New(muxSelectUartV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("muxSelectSpi"),
           FunctionTemplate::New(muxSelectSpiV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("muxSelectI2c"),
           FunctionTemplate::New(muxSelectI2cV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("variantPinMode"),
           FunctionTemplate::New(variantPinModeV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("variantPinModeIRQ"),
           FunctionTemplate::New(variantPinModeIRQV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("turnOffPWM"),
           FunctionTemplate::New(turnOffPWMV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("turnOnPWM"),
           FunctionTemplate::New(turnOnPWMV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("variantEnableFastGpio"),
           FunctionTemplate::New(variantEnableFastGpioV8)->GetFunction());

    obj->Set(v8::String::NewSymbol("variantEnablePullup"),
           FunctionTemplate::New(variantEnablePullupV8)->GetFunction());
}


// Const defined by macros
static void SetConst(Handle<Object> obj) {

    obj->Set(v8::String::NewSymbol("LINUX_BOOTLOADER_TTY"),
             v8::String::New("/dev/ttyGS0"));

    obj->Set(v8::String::NewSymbol("LINUX_SPIDEV"),
             v8::String::New("/dev/spidev1.0"));

    obj->Set(v8::String::NewSymbol("LINUX_EEPROM"),
             v8::String::New("/sys/bus/i2c/devices/0-0050/eeprom"));

    obj->Set(v8::String::NewSymbol("LINUX_ADC_FMT"),
             v8::String::New("/sys/bus/iio/devices/iio:device0/in_voltage%d_raw"));

    obj->Set(v8::String::NewSymbol("PLATFORM_ID"),
             Int32::New(0x06));

    obj->Set(v8::String::NewSymbol("ADC_RESOLUTION"),
             Int32::New(12));

    obj->Set(v8::String::NewSymbol("MAX_VARIANT_HPET_FREQ_HZ"),
             Int32::New(1000));

    obj->Set(v8::String::NewSymbol("MUX_SEL_NONE"),
             Int32::New(-1));

    obj->Set(v8::String::NewSymbol("MUX_SEL_UART0_RXD"),
             Int32::New(0));

    obj->Set(v8::String::NewSymbol("MUX_SEL_UART0_TXD"),
             Int32::New(1));

    obj->Set(v8::String::NewSymbol("MUX_SEL_SPI1_SS_B"),
             Int32::New(10));

    obj->Set(v8::String::NewSymbol("MUX_SEL_SPI1_MOSI"),
             Int32::New(11));

    obj->Set(v8::String::NewSymbol("MUX_SEL_SPI1_MISO"),
             Int32::New(12));

    obj->Set(v8::String::NewSymbol("MUX_SEL_SPI1_SCK"),
             Int32::New(13));

    obj->Set(v8::String::NewSymbol("MUX_SEL_AD7298_VIN0"),
             Int32::New(14));

    obj->Set(v8::String::NewSymbol("MUX_SEL_AD7298_VIN1"),
             Int32::New(15));

    obj->Set(v8::String::NewSymbol("MUX_SEL_AD7298_VIN2"),
             Int32::New(16));

    obj->Set(v8::String::NewSymbol("MUX_SEL_AD7298_VIN3"),
             Int32::New(17));

    obj->Set(v8::String::NewSymbol("MUX_SEL_AD7298_VIN4"),
             Int32::New(18));

    obj->Set(v8::String::NewSymbol("MUX_SEL_AD7298_VIN5"),
             Int32::New(19));

    obj->Set(v8::String::NewSymbol("MUX_SEL_I2C"),
             Int32::New(18));

    obj->Set(v8::String::NewSymbol("MUX_DEPTH_DIGITAL"),
             Int32::New(0x02));

    obj->Set(v8::String::NewSymbol("MUX_DEPTH_ANALOG"),
             Int32::New(0x01));

    obj->Set(v8::String::NewSymbol("MUX_DEPTH_UART"),
             Int32::New(0x02));

    obj->Set(v8::String::NewSymbol("MUX_DEPTH_SPI"),
             Int32::New(0x03));

    obj->Set(v8::String::NewSymbol("MUX_DEPTH_I2C"),
             Int32::New(0x01));

    obj->Set(v8::String::NewSymbol("GPIO_TOTAL"),
             Int32::New(56));

    obj->Set(v8::String::NewSymbol("GPIO_FAST_IO2"),
             Int32::New(0x40));

    obj->Set(v8::String::NewSymbol("GPIO_FAST_IO3"),
             Int32::New(0x80));

}

// Const defined by enumeration
static void SetEnumConst(Handle<Object> obj) {

}
static void SetGlobalVarFunc(Handle<Object> obj) {
}

void Initvariant_norm(Handle<Object> exports) {

    SetMemberFunc(exports);

    SetConst(exports);

    SetEnumConst(exports);

    SetGlobalVarFunc(exports);
}
