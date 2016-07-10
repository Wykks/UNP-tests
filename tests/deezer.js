var common = require("../common");
var prepare = common.prepare;
var finalize = common.finalize;
var expect = common.expect;

it('deezer', function*() {
    yield global.nightmare.goto('http://www.deezer.com/album/7261054');
    yield prepare('deezer');
    yield global.nightmare.click('#page_naboo_album li.action-item.action-force');
    var data = yield finalize();
    expect(data.nowPlaying).to.equal('The Rickrollerz - Never Gonna Give You Up');
    expect(data.trackName).to.equal('Never Gonna Give You Up');
    expect(data.duration).to.equal('00:30');
    expect(data.artistName).to.equal('The Rickrollerz');
    expect(data.url).to.equal('http://www.deezer.com/album/7261054');
});
