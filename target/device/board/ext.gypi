
#skeleton of node-gyp file

{
    'includes' : ['../libio/setting.gypi'],

    'variables': {
      'lib_root' : '../libio',
    },

    'dependencies': [
      '<(lib_root)/libio.gyp:libio',
    ],


}

