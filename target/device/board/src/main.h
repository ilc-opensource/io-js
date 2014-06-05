
#ifndef MAIN_H
#define MAIN_H

#include <node.h>
#include <v8.h>

using namespace v8;

extern void Initfast_gpio_sc(Handle<Object> exports);
extern void Initpin_map_norm(Handle<Object> exports);
extern void InitArduino(Handle<Object> exports);
extern void InitServo(Handle<Object> exports);
extern void InitOSAbstract_norm(Handle<Object> exports);
extern void Initpins_arduino(Handle<Object> exports);
extern void Initwiring_digital_norm(Handle<Object> exports);
extern void InitAnalogIO(Handle<Object> exports);
extern void Initsysfs(Handle<Object> exports);
extern void Initi2c(Handle<Object> exports);
extern void Initversion(Handle<Object> exports);
extern void Initvariant_norm(Handle<Object> exports);

#endif
