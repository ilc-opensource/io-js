var config = module.exports;

config["browser-emu"] = {
    rootPath: "../",
    environment: "browser", 
    sources: [
        "target/companion/lib/jquery/jquery.js",
        "bundle.js",
        "test/config.js",
        "test/emu.js"
    ],
    tests: [
        "test/tests/*.js"
    ]
};

config["browser-rpc-sync"] = {
    rootPath: "../",
    environment: "browser", // or "node"
    sources: [
        "target/companion/lib/jquery/jquery.js",
        "bundle.js",
        "test/config.js",
        "test/rpc_sync.js"
    ],
    tests: [
        "test/tests/*.js",
        "test/offload/*.js"
    ]
};

config["browser-rpc-async"] = {
    rootPath: "../",
    environment: "browser", // or "node"
    sources: [
        "target/companion/lib/jquery/jquery.js",
        "bundle.js",
        "test/config.js",
        "test/rpc_async.js"
    ],
    tests: [
        "test/tests/*.js",
        "test/offload/*.js"
    ]
};


config["node-emu"] = {
    rootPath: "../",
    environment: "node", // or "node"
    sources: [
        "test/emu.js"
    ],
    tests: [
        "test/tests/*.js"
    ]
};
/*
config["node-native"] = {
    rootPath: "../",
    environment: "node", // or "node"
    sources: [
        "test/native.js"
    ],
    tests: [
        "test/tests/*.js",
        "test/offload/*.js"
    ]
};
*/
config["node-rpc-sync"] = {
    rootPath: "../",
    environment: "node", // or "node"
    sources: [
        "test/rpc_sync.js"
    ],
    tests: [
        "test/tests/*.js",
    ]
};

config["node-rpc-async"] = {
    rootPath: "../",
    environment: "node", // or "node"
    sources: [
        "test/rpc_async.js"
    ],
    tests: [
        "test/tests/*.js"
    ]
};


