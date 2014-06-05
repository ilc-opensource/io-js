
#include "main.h"

void exportV8(Handle<Object> exports) {

    Initfast_gpio_sc(exports);
    Initpin_map_norm(exports);
    InitArduino(exports);
    InitServo(exports);
    InitOSAbstract_norm(exports);
    Initpins_arduino(exports);
    Initwiring_digital_norm(exports);
    InitAnalogIO(exports);
    Initsysfs(exports);
    Initi2c(exports);
    Initversion(exports);
    Initvariant_norm(exports);

}

NODE_MODULE(galileo, exportV8)
