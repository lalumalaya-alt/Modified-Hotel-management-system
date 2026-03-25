const babel = require('@babel/core');
const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');
const regex = /<script type="text\/babel">([\s\S]*?)<\/script>/i;
const match = html.match(regex);
if (match) {
  try {
    babel.transformSync(match[1], { presets: ['@babel/preset-react'] });
    console.log("Syntax is OK");
  } catch(e) {
    console.log("Error:", e.message);
  }
}
