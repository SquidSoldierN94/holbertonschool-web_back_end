/**
 * Class representing a currency.
 */
export default class Currency {
    /**
     * Create a new Currency instance.
     * @param {string} code - The code of the currency (e.g., '$').
     * @param {string} name - The name of the currency (e.g., 'Dollars').
     */
    constructor(code, name) {
      this.code = code; // Calls the setter for code
      this.name = name; // Calls the setter for name
    }
  
    /**
     * Getter for the 'code' attribute.
     * @returns {string} The code of the currency.
     */
    get code() {
      return this._code;
    }
  
    /**
     * Setter for the 'code' attribute.
     * Ensures 'code' is a string.
     * @param {string} value - The new code of the currency.
     * @throws {TypeError} Throws an error if value is not a string.
     */
    set code(value) {
      if (typeof value !== 'string') {
        throw new TypeError("Code must be a string");
      }
      this._code = value;
    }
  
    /**
     * Getter for the 'name' attribute.
     * @returns {string} The name of the currency.
     */
    get name() {
      return this._name;
    }
  
    /**
     * Setter for the 'name' attribute.
     * Ensures 'name' is a string.
     * @param {string} value - The new name of the currency.
     * @throws {TypeError} Throws an error if value is not a string.
     */
    set name(value) {
      if (typeof value !== 'string') {
        throw new TypeError("Name must be a string");
      }
      this._name = value;
    }
  
    /**
     * Method to display the full currency in the format "name (code)".
     * @returns {string} The full currency display.
     */
    displayFullCurrency() {
      return `${this.name} (${this.code})`;
    }
  }
  