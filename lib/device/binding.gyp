{
  'targets' : [{

    'target_name' : 'arduiPIA',

    'sources' : [
      './src/arduiPIA.cpp'
    ],

    'include_dirs' : [
      '../../c_decl',
      '../../../pia-sdk-repo/iolib/core',
      '../../../pia-sdk-repo/iolib/lib',
      '../../../pia-sdk-repo/iolib/board',
      '../../../pia-sdk-repo/iolib/arduino',
      '../../../pia-sdk-repo/iolib/drv'
    ],

    'libraries' : [
      '-L../../../../pia-sdk-repo/iolib',
      '-lpia-iolib'
    ]
  }]
}
