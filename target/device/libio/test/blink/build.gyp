{
  'targets': [{

    'dependencies': [
      '../../libio.gyp:libio',
    ],

    'variables': {
      'lib_root' : '../..',
    },

    'includes' : ['../../setting.gypi'],
    'target_name': 'blink',
    'type': 'executable',

    'sources' : [
      'Blink.cpp'
    ],

    'libraries' : [
      '-lm',
      '-lpthread'
    ],
  }],
}

