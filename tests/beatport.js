var common = require("../common");
var prepare = common.prepare;
var finalize = common.finalize;
var expect = common.expect;

it('beatport', function*() {
    yield global.nightmare.goto('https://www.beatport.com/track/in-the-reds-original-mix/7995360');
    yield prepare('beatport');
    yield global.nightmare.click('.interior-track-actions > .playable-play')
    var data = yield finalize();
    expect(data.nowPlaying).to.equals("CIREZ D - IN THE REDS");
});
