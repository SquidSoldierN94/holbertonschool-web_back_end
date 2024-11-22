/**
 * Function to demonstrate block scoping with let and const
 * @param {boolean} trueOrFalse - A boolean parameter to control the if block execution
 * @returns {Array} - An array containing the values of task and task2
 */
export default function taskBlock(trueOrFalse) {
  // Declare task and task2 using let to ensure block scoping within the function
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    // Declare new block-scoped constants within the if block
    // These will not overwrite the outer task and task2 variables
    const task = true;
    const task2 = false;
  }

  // Return the outer scoped variables task and task2
  return [task, task2];
}
