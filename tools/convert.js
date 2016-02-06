var dict = require('./dict-zi.js')
var fs   = require('fs')

var s = ''
for(var p in dict) {
    if(dict.hasOwnProperty(p)) {
        var hanzi = String.fromCharCode(p)
        var pinyin = dict[p]
        s = s + hanzi + '=' + pinyin + '\n'

    }
}

 fs.writeFile('./dict-zi.db', s, function(err){
        if(err) throw err;
        console.log('has finished');
    });
    