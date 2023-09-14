export default function appendToEachArrayValue(array, appendString) {
  const Narrays = [];
  for (const value of array) {
    Narrays.push(appendString + value)
  }
  return array;
}
