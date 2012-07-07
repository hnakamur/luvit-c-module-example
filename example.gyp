{
  'targets': [
    {
      'target_name': 'example',
      'type': 'loadable_module',
      'sources': [
        'example.c'
      ],
      'conditions': [
        [
          'OS=="mac"', {
            'xcode_settings': {
              'ARCHS': [ 'x86_64' ],
            },
            'libraries': [ '-undefined dynamic_lookup' ],
            'defines': [
              'PLATFORM="<(OS)"',
              '_LARGEFILE_SOURCE',
              '_FILE_OFFSET_BITS=64',
            ]
          }
        ]
      ]
    }
  ]
}
