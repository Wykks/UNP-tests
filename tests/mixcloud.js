var common = require("../common");
var prepare = common.prepare;
var finalize = common.finalize;
var expect = common.expect;

it('mixcloud', function*() {
    yield global.nightmare.goto('https://www.mixcloud.com/truthoughts/');
    yield prepare('mixcloud');
    yield global.nightmare.click('.play-all-button');
    var data = yield finalize();
    expect(data.nowPlaying).to.match(/^Tru Thoughts - .+$/);
    yield global.nightmare.click('.player-control.pause-state');
});
