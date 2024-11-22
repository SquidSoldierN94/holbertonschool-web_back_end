/**
 * Class representing an Airport.
 */
export default class Airport {
    /**
     * Create a new Airport instance.
     * @param {string} name - The name of the airport.
     * @param {string} code - The airport code.
     */
    constructor(name, code) {
      this._name = name; // Store the airport name
      this._code = code; // Store the airport code
    }
  
    /**
     * Override the default toString method to return the airport code.
     * @returns {string} The string representation of the airport.
     */
    toString() {
      return `[object ${this._code}]`;
    }
  }
  