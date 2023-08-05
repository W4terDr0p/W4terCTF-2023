const express = require('express')
const app = express()
const port = 80
const path = require('path');
const { readFile } = require('fs/promises')
const puppeteer = require('puppeteer')

var invoice = null

app.use(express.urlencoded({ extended: true }));
app.use(express.static('static'))

//根目录
app.get('/', (_, res) => {
  res.sendFile('index.html', { root: path.join(__dirname, 'templates') })
})

//the space for u to confession
app.get('/confession', (_, res) => {
  res.sendFile('confession.html', { root: path.join(__dirname, 'templates') })
})


app.get('/render', async (req, res) => {
  if (!invoice) {
    invoice = await readFile('templates/render.html', 'utf8')
  }

  const blacklist = [
    /on/i, /localStorage/i, /alert/, /fetch/, /XMLHttpRequest/, /window/, /location/, /document/
  ]

  for (const key in req.query) {
    for (const item of blacklist) {
      if (item.test(key.trim()) || item.test(req.query[key].trim())) {
        req.query[key] = ""
      }
    }
  }

  console.log(req.query.word)

  const html = invoice.replaceAll("{{ word }}", req.query.word)

  res.send(html)

  try {
    const browser_options = {
      args: [
        '--disable-background-networking',
        '--disable-default-apps',
        '--no-sandbox',
        '--disable-extensions',
        '--disable-gpu',
        '--disable-sync',
        '--disable-translate',
        '--hide-scrollbars',
        '--metrics-recording-only',
        '--mute-audio',
        '--no-first-run',
        '--safebrowsing-disable-auto-update'
      ],
      pipe: true,
      headless: true
    };
    const delay = ms => new Promise(resolve => setTimeout(resolve, ms))
    const browser = await puppeteer.launch(browser_options);
    const page = await browser.newPage();
    await page.goto('http://127.0.0.1/adminrender?word=' + req.query.word, { waitUntil: 'networkidle0' });
    await delay(1000)
    await browser.close();
  } catch (e) {
    console.log(e.message);
  }
})

app.get('/adminrender', async (req, res) => {
  if (!invoice) {
    invoice = await readFile('templates/render.html', 'utf8')
  }

  if (req.socket.remoteAddress == "::ffff:127.0.0.1") {
    const flag = process.env.GZCTF_FLAG
    const html = invoice
      .replaceAll("{{ word }}", req.query.word)
      .replaceAll("{{ flag }}", flag)
    res.send(html)
  } else {
    const html = invoice
      .replaceAll("{{ word }}", req.query.word)
      .replaceAll("{{ flag }}", "tel-114514")
    res.send(html)
  }
})

app.listen(port, () => {
  console.log(`Feedback Box listening on port ${port}`)
})
