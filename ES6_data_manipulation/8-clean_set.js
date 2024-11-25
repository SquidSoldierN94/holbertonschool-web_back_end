export default function cleanSet(set, startString) {
  if (startString === '') return '';

  const ArrayToModify = Array.from(set);

  const FilteredArray = ArrayToModify.filter((words) => words.startsWith(startString));
  const ArrayWithoutPrefix = FilteredArray.map((words) => words.slice(startString.length));

  const resultString = ArrayWithoutPrefix.join('-');
  return resultString;
}
