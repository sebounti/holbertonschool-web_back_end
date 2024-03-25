// task 0-calcul.js
function calculateNumber(a, b) {
  if (typeof a !== "number" || typeof b !== "number") {
    throw new TypeError("All arguments must be numbers");
  }

  const rounded_a = Math.round(a);
  const rounded_b = Math.round(b);
  return rounded_a + rounded_b;
}

module.exports = calculateNumber;
