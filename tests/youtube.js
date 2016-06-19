var common = require("../common");
var prepare = common.prepare;
var finalize = common.finalize;
var expect = common.expect;

it('youtube', function*() {
    yield global.nightmare.goto('https://www.youtube.com/watch?v=dQw4w9WgXcQ');
    yield prepare('youtube');
    var data = yield finalize();
    expect(data.nowPlaying).to.equal('Rick Astley - Never Gonna Give You Up');
});
