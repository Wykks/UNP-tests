var chai = require("chai");

var options = require('./config.json');

function* prepare(website) {
    yield global.nightmare
        .inject('js', './Untamed-Now-Playing-Next/data/third-party/jquery-2.1.3.min.js')
        .evaluate(() => {
            window.UNPBrowserFunc = class {
                static updateNowPlaying(data) {
                    $(document).data('UNP', data);
                }
                static getOptions() {
                    return new Promise((resolve) => {
                        resolve({
                            unpDisableYoutube: false
                        })
                    });
                }
            }
        })
        .inject('js', './Untamed-Now-Playing-Next/data/common/websites-support/website.js')
        .inject('js', `./Untamed-Now-Playing-Next/data/common/websites-support/websites/${website}.js`)
}

function* finalize() {
    yield global.nightmare.wait(() => {
        return $(document).data('UNP') !== undefined;
    });
    return global.nightmare.evaluate(() => {
        return $(document).data('UNP');
    });
}

exports.prepare = prepare;
exports.finalize = finalize;
exports.options = options;
exports.chai = chai;
exports.expect = chai.expect;
