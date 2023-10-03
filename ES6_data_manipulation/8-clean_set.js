export default function cleanset(set, startstring) {
  const result = [];
  for (const item of set) {
    if (item.startsWith(startstring)) {
      result.push(item.slice(startstring.length));
    }
  }
  return result.join('-');
}
