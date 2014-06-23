{
  'targets' : [{

    'dependencies' : [
     ],

    'includes' : ['./setting.gypi'],

    'variables' : {

      'lib_root' : '.',

      'export_headers' : [
        '<(core_dir)/AnalogIO.h',
        '<(core_dir)/Arduino.h',
        '<(core_dir)/RingBuffer.h',
        '<(core_dir)/TTYUART.h',
        '<(core_dir)/UtilTime.h',
        '<(core_dir)/fast_gpio_sc.h',
        '<(core_dir)/i2c.h',
        '<(core_dir)/interrupt.h',
        '<(core_dir)/sysfs.h',

        '<(variant_dir)/pins_arduino.h',

        '<(extra_dir)/OSAbstract_norm.h',
        '<(extra_dir)/Wire_norm.h',
        '<(extra_dir)/variant_norm.h',
        '<(extra_dir)/version.h',
        '<(extra_dir)/wiring_digital_norm.h',

        '<(lib_dir)/Servo/Servo.h',
        '<(lib_dir)/SPI/SPI.h',
      ],
    },

    'target_name' : 'export',
    'type': 'static_library',

    'sources' : [
    ],

    'copies' : [
      {
        'destination' : './export',
         'files': ['<@(export_headers)']
      }
    ],

  }]
}

