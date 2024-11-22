/**
 * Class representing a HolbertonClass.
 */
export default class HolbertonClass {
    /**
     * Create a new HolbertonClass instance.
     * @param {number} size - The size of the class.
     * @param {string} location - The location of the class.
     */
    constructor(size, location) {
      this._size = size;       // Store the size
      this._location = location; // Store the location
    }
  
    /**
     * Override the [Symbol.toPrimitive] method to define custom type casting.
     * @param {string} hint - The type we are trying to cast to (either "string" or "number").
     * @returns {string|number} The appropriate primitive value for the class.
     */
    [Symbol.toPrimitive](hint) {
      if (hint === 'number') {
        return this._size; // Return the size when cast to a number
      } else if (hint === 'string') {
        return this._location; // Return the location when cast to a string
      }
      return null; // Return null for any other hints (though this case is not typically used)
    }
  }
  