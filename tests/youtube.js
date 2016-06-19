var common = require("../common");
var inject = common.inject;
var expect = common.expect;

it('youtube', function*() {
    yield global.nightmare.goto('https://www.youtube.com/watch?v=dQw4w9WgXcQ');
    yield inject('youtube');
    var data = yield global.nightmare
            .wait(() => {
                return $(document).data('UNP') !== undefined;
            })
            .evaluate(() => {
                return $(document).data('UNP');
            })
    expect(data.nowPlaying).to.equal('Rick Astley - Never Gonna Give You Up');
});
