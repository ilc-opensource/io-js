{
  'variables' : {

    'VER'         : '1.5.3',
    'arduino_root': '<(lib_root)/arduino',
    'core_dir'    : '<(arduino_root)/x86/cores/arduino',
    'variant_dir' : '<(arduino_root)/x86/variants/galileo_fab_d',
    'lib_dir'     : '<(arduino_root)/x86/libraries', 
    'extra_dir'   : './src',

    'lib_inc' : [
      '<(lib_dir)/Servo',
      '<(lib_dir)/Wire',
      '<(lib_dir)/SPI',
    ],
  },

  'include_dirs' : [
    '<@(core_dir)',
    '<@(variant_dir)',
    '<@(lib_inc)',
    '<@(extra_dir)',
  ],


  'cflags' : [
    '-g -Os',
    '-w -ffunction-sections -fdata-sections -MMD'
  ],

  'cflags_c' : [
  ],

  'cflags_cc': [
    '-fno-exceptions'
  ],

  'cflags!_cc' : [
  ],

}
