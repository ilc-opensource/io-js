{
  'targets' : [{

    'dependencies' : [
     ],

    'includes' : ['./setting.gypi'],

    'variables' : {

      'lib_root' : '.',

      'core_srcs'   : [
        '<(core_dir)/fast_gpio_sc.c',
        '<(core_dir)/i2c.c',
        '<(core_dir)/interrupt.c',
        '<(core_dir)/mux.c',
        '<(core_dir)/sysfs.c',
        '<(core_dir)/wiring_analog.c',
        '<(core_dir)/wiring_digital.c',
        '<(core_dir)/IPAddress.cpp',
        '<(core_dir)/Print.cpp',
        '<(core_dir)/RingBuffer.cpp',
        '<(core_dir)/Stream.cpp',
        '<(core_dir)/TTYUART.cpp',
        '<(core_dir)/UtilTime.cpp',
        '<(core_dir)/WMath.cpp',
        '<(core_dir)/WString.cpp',
        '<(core_dir)/main.cpp',
        '<(core_dir)/trace.cpp',
      ],

      'variant_srcs' : [
        '<(variant_dir)/variant.cpp'
      ],

      'lib_srcs' : [
        '<(lib_dir)/Servo/Servo.cpp',
        '<(lib_dir)/Wire/Wire.cpp'
      ], 

      'lib_inc' : [
        '<(lib_dir)/Servo',
        '<(lib_dir)/Wire'
      ],

      'extra_srcs' : [
        '<(extra_dir)/OSAbstract_norm.cpp',
        '<(extra_dir)/version.cpp',
      ],
 
      'export_headers' : [
        '<(core_dir)/Arduino.h',
        '<(core_dir)/i2c.h',        
        '<(core_dir)/AnalogIO.h',
        '<(core_dir)/fast_gpio_sc.h',
        '<(core_dir)/sysfs.h',

        '<(variant_dir)/pins_arduino.h',

        '<(extra_dir)/OSAbstract_norm.h',
        '<(extra_dir)/wiring_digital_norm.h',
        '<(extra_dir)/variant_norm.h',
        '<(extra_dir)/pin_map_norm.h',
        '<(extra_dir)/version.h',

        '<(lib_dir)/Servo/Servo.h',
      ],
    },

    'target_name' : 'libio',
    'type': 'static_library',

    'sources' : [
      '<@(core_srcs)',
      '<@(variant_srcs)',
      '<@(lib_srcs)',
      '<@(extra_srcs)',
    ],

  }]
}

