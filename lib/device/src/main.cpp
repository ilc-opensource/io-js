
#include "main.h"

void exportV8(Handle<Object> exports) {

    InitAnalogIO(exports);
    Initi2c(exports);
    Initpins_arduino(exports);
    Initversion(exports);
    Initwiring_digital_norm(exports);
    Initsysfs(exports);
    Initfast_gpio_sc(exports);
    InitOSAbstract_norm(exports);
    Initversion_export(exports);
    InitUtilTime(exports);
    Initvariant_norm(exports);
    Initpin_map_norm(exports);
    InitArduino(exports);
    InitServo(exports);

}

NODE_MODULE(galileo, exportV8)
