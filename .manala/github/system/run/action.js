const system = require('../module');
const core = system.core

system.run({
    'dir': core.getInput('dir'),
    'docker_dir': core.getInput('docker_dir'),
    'docker_env': core.getInput('docker_env'),
    'run': core.getInput('run'),
});
