module.exports = {
  "extends": [
    "stylelint-scss",
    "stylelint-config-recommended",
    "stylelint-config-rational-order"
  ],
  "rules": {
    "at-rule-no-unknown": [true, {
      "ignoreAtRules": ["debug","warn", "function", "if", "else", "each", "include", "extend", "mixin", "return", "for"]
    }],
    "no-descending-specificity": null,
    "indentation": 2,
    "color-hex-case": "lower",
    "plugin/rational-order": [true, {
      "border-in-box-model": false,
      "empty-line-between-groups": true,
    }]
  }
};