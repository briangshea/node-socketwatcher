{
  "targets": [
    {
      "target_name": "socketwatcher",
      "sources": [ "socket_watcher.cpp" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ]
    },
    {
      "target_name": "socketwatcher-package",
      "type": "none",
      "dependencies": [ "socketwatcher" ],
      "copies": [
        { "destination": "./package",
          "files": ['./build/Release/socketwatcher.node']
        }
      ]
    }
  ]
}
