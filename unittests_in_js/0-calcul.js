// task 0-calcul.js
function calculateNumber(a, b) {
  if (typeof a !== "number" || typeof b !== "number" || isNaN(a) || isNaN(b)) {
    throw new TypeError("All arguments must be numbers");
  }

  let rounded_a = Math.round(a);
  let rounded_b = Math.round(b);
  return rounded_a + rounded_b;
}

module.exports = calculateNumber;
