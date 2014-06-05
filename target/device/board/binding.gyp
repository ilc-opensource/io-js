
#skeleton of node-gyp file

{
  'targets' : [{

    'target_name' : 'galileo',

    'sources' : [
      'src/variant_norm_addon.cpp',
      'src/OSAbstract_norm_addon.cpp',
      'src/sysfs_addon.cpp',
      'src/AnalogIO_addon.cpp',
      'src/Servo_addon.cpp',
      'src/Arduino_addon.cpp',
      'src/pins_arduino_addon.cpp',
      'src/pin_map_norm_addon.cpp',
      'src/fast_gpio_sc_addon.cpp',
      'src/version_addon.cpp',
      'src/i2c_addon.cpp',
      'src/wiring_digital_norm_addon.cpp',
      'src/main.cpp',
      'src/_callback.cpp'
      
    ],

    'include_dirs' : [
      'src/',
      '../../target/device/libio/export',
      
    ],

    'libraries' : [
      #'-L/io/library/path/,
      #'-liolib'
    ],

    'includes': ['ext.gypi']

  }]
}
