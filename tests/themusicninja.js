var common = require("../common");
var prepare = common.prepare;
var finalize = common.finalize;
var expect = common.expect;

it('themusicninja', function*() {
    yield global.nightmare.goto('http://www.themusicninja.com/electronic-ninth-parallel-infinitum/');
    yield prepare('themusicninja');
    yield global.nightmare.click('#content .ninja_player');
    var data = yield finalize();
    expect(data.nowPlaying).to.equal('Ninth Parallel - Infinitum');
});
