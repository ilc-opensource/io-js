
#skeleton of node-gyp file

{
  'targets' : [{

    'target_name' : 'galileo',

    'sources' : [
      'src/Sample_addon.cpp',
      'src/arduiPIA_addon.cpp',
      'src/MultiClass_addon.cpp',
      'src/Servo_addon.cpp',
      'src/Arduino_addon.cpp',
          
    ],

    'include_dirs' : [
      'src/'
    ],

    'libraries' : [
      #'-L/io/library/path/,
      #'-liolib'
    ]

  }]
}
