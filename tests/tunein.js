var common = require("../common");
var prepare = common.prepare;
var finalize = common.finalize;
var expect = common.expect;

it.only('tunein', function*() {
    yield global.nightmare.goto('http://tunein.com/radio/Cherry-Radio-s189943/');
    yield prepare('tunein');
    var data = yield finalize();
    expect(data.nowPlaying).to.match(/Cherry Radio/);
});
