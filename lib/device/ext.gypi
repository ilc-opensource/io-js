
#skeleton of node-gyp file

{

    #'target_name' : 'galileo',

    'variables' : {
      'arduino_path': '../../../arduino-1.5.3',
      'libio_path'  : '../../../libio'
    },

    'include_dirs' : [
      "<(arduino_path)/hardware/arduino/x86/cores/arduino/",
      "<(arduino_path)/hardware/arduino/x86/variants/galileo_fab_d/",
      "<(arduino_path)/hardware/arduino/x86/libraries/Wire/",
      "<(arduino_path)/hardware/arduino/x86/libraries/Servo/"
    ],

    'libraries' : [
      '../<(libio_path)/lib/libio.a'
    ]

}

