
#skeleton of node-gyp file

{

    'target_name' : 'pia',

    'variables' : {
      'libio_path'  : '/home/rfen/workspace/pia-sdk-0225/iolib/'
    },

    'include_dirs' : [
      "<(libio_path)/arduino",
      "<(libio_path)/core",
      "<(libio_path)/drv",
      "<(libio_path)/board",
    ],

    'libraries' : [
      '<(libio_path)/libpia-iolib.a'
    ]

}

