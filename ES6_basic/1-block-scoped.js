/**
 * Function to demonstrate block scoping with const
 * @param {boolean} trueOrFalse - A boolean parameter to control the if block execution
 * @returns {Array} - An array containing the values of task and task2
 */
export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = true;
    const task2 = false;
  }

  return [task, task2];
}
