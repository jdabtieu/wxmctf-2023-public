process.env.NODE_ENV = "production";

const express = require("express");
const sqlite3 = require('sqlite3');

let db = new sqlite3.Database('data.db', sqlite3.OPEN_READONLY, (err) => {
    if (err) {
        console.error(err.message);
    }
    console.log('Connected to the database');
});

const app = express();
const PORT = 8080;

app.use(express.urlencoded({ extended: true }));
app.set('view engine', 'ejs');

app.post('/search', (req, res) => {
    //console.log(`SELECT * FROM skins WHERE skinid = '${filter(req.body.query)}' OR name = '${filter(req.body.query)}'`);
    db.get(`SELECT * FROM skins WHERE skinid = '${filter(req.body.query)}' OR name = '${filter(req.body.query)}'`, (err, row) => {
        if (err) {
            //console.log(err);
            res.redirect('/');
        } else {
            res.render('search', {skin: row});
        }
    });
});

app.get("/", (req, res) => {
    res.render('index');
});

app.get("/*", (req, res) => {
    res.redirect('/');
});

app.listen(PORT, () => {
    console.log(`Listening on port ${PORT}`);
});

function filter(text) {
    return text.replace(new RegExp("--", "g"), "").replace(new RegExp(";", "g"), "");
}
