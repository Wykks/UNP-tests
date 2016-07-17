var common = require("../common");
var prepare = common.prepare;
var finalize = common.finalize;
var expect = common.expect;

it('loopmasters', function*() {
    yield global.nightmare.goto('http://www.loopmasters.com/genres/66-Tech-House/products/5108-Modern-Tech-House-Vol-II');
    yield prepare('loopmasters');
    yield global.nightmare.click('.demoloops-content > .demoloop:first-child');
    var data = yield finalize();
    expect(data.nowPlaying).to.equal("Samplestate - Modern Tech House Vol. II");
});
