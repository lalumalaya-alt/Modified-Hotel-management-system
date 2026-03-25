const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');

try {
  const dom = new JSDOM(html);
  // Just seeing if there's an obvious syntax error in the script tags that Babel would catch
  // but it's JSX, so normal JSDOM won't execute it correctly anyway without Babel translation
  console.log("JSDOM parsed");
} catch(e) {
  console.log(e);
}
