#!/usr/bin/node
/* a script that concats 2 files */

const fs = require('fs');
let data = '';

data = data.concat(fs.readFileSync(process.argv[2]));
data = data.concat(fs.readFileSync(process.argv[3]));

fs.writeFileSync(process.argv[4], data);
