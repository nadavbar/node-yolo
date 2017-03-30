{
  "variables": {
    'with_opencv%': '<!(node ./util/has_lib.js opencv)',
    'with_cuda%': '<!(node ./util/has_lib.js cuda)'
  },
  "targets": [
    {
      "target_name": "darknet",
      "sources": [
        "darknet.cc",
        "src/demo.cc"
      ],
      "include_dirs": [
        "./src",
        "<!(node -e \"require('nan')\")",
      ],
      "cflags": [
        "-Wall",
        "-Wfatal-errors",
        "-fPIC",
        "-Ofast"
      ],
      "conditions": [
        ['with_opencv=="true"', {
          "defines": [
            "OPENCV",
          ],
          "libraries": [
            "-lopencv_core",
            "-lopencv_highgui"
          ]
        }],
        ['with_cuda=="true"', {
          "defines": [
            "GPU"
          ],
          "libraries": [
            "-L/usr/local/cuda/lib",
            "-lcuda",
            "-lcudart",
            "-lcublas",
            "-lcurand"
          ],
          "include_dirs": [
            "./src",
            "<!(node -e \"require('nan')\")",
            "/usr/local/cuda/include"
          ],
        }],
          [ 'OS=="win"', {
            'include_dirs': [
              'C:/opencv_2.4.9/opencv/build/include',
              'win/3rdparty/include',
              'win/darknet/include',
          ],
          "defines": [
            "_TIMESPEC_DEFINED"
          ],
          "libraries" : [
                "-l../win/darknet/lib/$(Platform)/darknet.lib",
                "-l../win/3rdparty/lib/$(Platform)/pthreadVC2.lib",
                "-lC:/opencv_2.4.9/opencv/build/x64/vc12/lib/opencv_highgui249.lib",
                "-lC:/opencv_2.4.9/opencv/build/x64/vc12/lib/opencv_core249.lib"
          ]
        }, {
          "libraries": [
            "-lm",
            "-lpthread",
            "-lstdc++",
            "-ldarknet"
          ]
        }]
      ]
    }
  ]
}