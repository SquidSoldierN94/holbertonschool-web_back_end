export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }

  const resultArray = [];

  for (const value of set) {
    if (value.startsWith(startString)) {
      resultArray.push(value.slice(startString.length));
    }
  }

  return resultArray.join('-');
}
