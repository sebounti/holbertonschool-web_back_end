// task 0-calcul.js
function calculateNumber(a, b) {
  if (typeof a !== "number" || typeof b !== "number" || isNaN(a) || isNaN(b)) {
    throw new TypeError("All arguments must be numbers");
  }
  return Math.rounded(a) + Math.rounded(b);
}

module.exports = calculateNumber;
