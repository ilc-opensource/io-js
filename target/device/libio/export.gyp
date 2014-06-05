{
  'targets' : [{

    'dependencies' : [
     ],

    'includes' : ['./setting.gypi'],

    'variables' : {

      'lib_root' : '.',

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

