var common = require("../common");
var prepare = common.prepare;
var finalize = common.finalize;
var expect = common.expect;
var options = common.options;

it.skip('spotify', function*() {
    yield global.nightmare.goto('https://play.spotify.com/album/2mCuMNdJkoyiXFhsQCLLqw');
    yield global.nightmare
        .click('#has-account')
        .type('#login-usr', options['websites']['spotify']['login'])
        .type('#login-pass', options['websites']['spotify']['pass'])
        .click('#sp-login-form > div > button')
        .wait('#main-nav')
    yield prepare('spotify');
    // yield global.nightmare.wait('button.button-play')
    //     .click('button.button-play');
    var data = yield finalize();
    expect(data.nowPlaying).to.equal('Rick Astley - Never Gonna Give You Up');
});
