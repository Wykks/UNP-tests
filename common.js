var chai = require("chai");

var options = {
    test: 'test'
};

function inject(website) {
    return global.nightmare
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

exports.inject = inject;
exports.options = options;
exports.chai = chai;
exports.expect = chai.expect;
