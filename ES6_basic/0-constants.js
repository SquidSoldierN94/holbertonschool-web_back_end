/**
 * Function to return a constant string.
 * Uses const to declare the task variable.
 *
 * @returns {string} The string 'I prefer const when I can.'
 */
export function taskFirst() {
    const task = 'I prefer const when I can.';
    return task;
  }
  
  /**
   * Function to return a string.
   *
   * @returns {string} The string ' is okay'
   */
  export function getLast() {
    return ' is okay';
  }
  
  /**
   * Function to return a combined string.
   * Uses let to declare the combination variable and modifies it.
   *
   * @returns {string} The combined string 'But sometimes let is okay'
   */
  export function taskNext() {
    let combination = 'But sometimes let';
    combination += getLast();
    return combination;
  }
  