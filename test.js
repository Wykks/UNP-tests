require('co-mocha');

const Nightmare = require('nightmare');
const fs = require('fs');

const tests = fs.readdirSync('./tests');

describe('UNP Tests', function() {
    this.timeout(30000);

    beforeEach(() => {
        global.nightmare = Nightmare({
            show: false,
            webPreferences: {
                plugins: true,
            },
            switches: {
                'ppapi-flash-path': '/opt/google/chrome/PepperFlash/libpepflashplayer.so'
            }
        });
    });

    tests.forEach((test) => {
        require(`./tests/${test}`)
    });

    afterEach(function*() {
        yield global.nightmare.end();
    });
});
