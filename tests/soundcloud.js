var common = require("../common");
var prepare = common.prepare;
var finalize = common.finalize;
var expect = common.expect;

it('soundcloud', function*() {
    yield global.nightmare.goto('https://soundcloud.com/nils-official/rick-astley-feat-avicii-never');
    yield prepare('soundcloud');
    var data = yield finalize();
    expect(data.nowPlaying).to.equal('AVICII vs RICK ASTLEY - Never Gonna Wake You Up (Get Knocked Down) (NilsOfficial Mashup)');
    expect(data.trackName).to.equal('Never Gonna Wake You Up (Get Knocked Down) (NilsOfficial Mashup)');
    expect(data.duration).to.equal('4:26');
    expect(data.artistName).to.equal('AVICII vs RICK ASTLEY');
    expect(data.url).to.equal('http://soundcloud.com/nils-official/rick-astley-feat-avicii-never');
});
