module.exports = {
  "env": {
    "browser": true,
    "es2021": true,
    "node": true,
    "jest": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:react/recommended",
    "plugin:react/jsx-runtime",
    // "plugin:testing-library/react",
    // "plugin:jest/all"
  ],
  "overrides": [],
  "parserOptions": {
    "ecmaVersion": "latest",
    "sourceType": "module",
    "requireConfigFile": false,
  },
  "plugins": [
    "react"
  ],
  "rules": {
    "no-unused-vars": "off"
  },
  "parser": "@babel/eslint-parser"
}
