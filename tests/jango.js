var common = require("../common");
var prepare = common.prepare;
var finalize = common.finalize;
var expect = common.expect;

it('jango', function*() {
    yield global.nightmare.goto('http://www.jango.com/music/Alan+Walker');
    yield prepare('jango');
    var data = yield finalize();
    expect(data.nowPlaying).to.match(/^Alan Walker - .+$/);
});
