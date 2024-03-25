// task 0-calcul.js
function calculateNumber(a, b) {
  if (typeof a !== "number" || typeof b !== "number" || isNaN(a) || isNaN(b)) {
    throw new TypeError("All arguments must be numbers");
  }
  return Math.round(a) + Math.round(b);
}

module.exports = calculateNumber;
