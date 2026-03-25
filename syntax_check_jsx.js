const fs = require('fs');
const babel = require('@babel/core');

const html = fs.readFileSync('index.html', 'utf8');

const regex = /<script type="text\/babel">([\s\S]*?)<\/script>/i;
const match = html.match(regex);

if (match) {
  const code = match[1];
  try {
    const result = babel.transformSync(code, {
      presets: ['@babel/preset-react'],
      filename: 'index.js'
    });
    console.log("React JSX Syntax is valid.");
  } catch (err) {
    console.error("Syntax Error in React Code:\n", err.message);
  }
} else {
  console.log("No React script tag found.");
}
