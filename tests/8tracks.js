var common = require("../common");
var prepare = common.prepare;
var finalize = common.finalize;
var expect = common.expect;

it('8tracks youtube', function*() {
    yield global.nightmare.goto('http://8tracks.com/kat-alx/read-sleep-breathe');
    yield prepare('8tracks');
    yield global.nightmare.click('#play_on_youtube');
    var data = yield finalize();
    expect(data.nowPlaying).to.equal('Brian Crain - Rain');
});

it('8tracks', function*() {
    yield global.nightmare.goto('http://8tracks.com/kat-alx/read-sleep-breathe#smart_id=all&play=1');
    yield prepare('8tracks');
    var data = yield finalize();
    expect(data.nowPlaying).to.equal('Brian Crain - Rain');
});
