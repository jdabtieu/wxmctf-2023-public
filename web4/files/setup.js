//this script adds the flag to the DB

const FLAG = process.env.FLAG ?? "wxmctf{dummy_flag}";
const sqlite3 = require('sqlite3');

let db = new sqlite3.Database('data.db', sqlite3.OPEN_READWRITE);

db.run(`INSERT INTO secretskins VALUES('gems', '${FLAG}', 'https://help.supercellsupport.com/uploads/bs-payments.png')`, () => {
    console.log('Done');
});
