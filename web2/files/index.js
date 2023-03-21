const express = require('express');
const app = express();

app.use(express.json());

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    try {
        if (!req.headers['user-agent'] || !req.headers['user-agent'].includes("lyonbrowser")) {
            res.render('view', { message: 'you dont look like a lyonbrowser user to me', flag: false });
        }
        else if (!req.headers['referer'] || req.headers['referer'] != "https://maclyonsden.com/") {
            res.render('view', { message: 'wlmac people come from the maclyonsden.com website, are you a spy?', flag: false });
        }
        else if (!req.headers['date'] || new Date(req.headers.date).getTime() < Date.now() + 315360000000) { // 10 years
            res.render('view', { message: 'you are a mere mortal who lives in the present. we are divine beings living 10 years in the future. we are not the same.', flag: false });
        }
        else if (!req.headers['upgrade-insecure-requests'] || req.headers['upgrade-insecure-requests'] != 1) { // much security
            res.render('view', { message: 'hey, you need to explicitly be SECURE', flag: false });
        }
        else if (!req.headers['downlink'] || isNaN(req.headers['downlink']) || parseInt(req.headers['downlink']) <= 10000) { // 10gbps LOL
            res.render('view', { message: 'imagine having slow internet', flag: false });
        }
        else {
            res.render('view', { message: `Here is the flag: ${process.env.FLAG ?? "wxmctf{dummy_flag}"}`, flag: true });
        }
    }
    catch {
        res.status(500).json({ status: 500, message: ":flooshed:" });
    }
})

app.use('/', (req, res) => {
    res.status(404).send('wut r u doing');
})

app.listen(3000, () => {
    console.log('server be runnin (port 3000)');
});
