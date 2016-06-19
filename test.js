require('co-mocha');

const Nightmare = require('nightmare');
const fs = require('fs');

const tests = fs.readdirSync('./tests');

describe('UNP Tests', function() {
    this.timeout(15000);

    beforeEach(function() {
        global.nightmare = Nightmare({
            show: false
        });
    });

    tests.forEach((test) => {
        require(`./tests/${test}`)
    });

    afterEach(function*() {
        yield global.nightmare.end();
    });
});
