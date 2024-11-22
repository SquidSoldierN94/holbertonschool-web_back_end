import Currency from './3-currency.js';

/**
 * Class representing a pricing structure.
 */
export default class Pricing {
  /**
   * Create a new Pricing instance.
   * @param {number} amount - The amount of the price.
   * @param {Currency} currency - The currency of the price.
   */
  constructor(amount, currency) {
    this.amount = amount; // Calls the setter for amount
    this.currency = currency; // Calls the setter for currency
  }

  /**
   * Getter for the 'amount' attribute.
   * @returns {number} The amount of the price.
   */
  get amount() {
    return this._amount;
  }

  /**
   * Setter for the 'amount' attribute.
   * Ensures 'amount' is a number.
   * @param {number} value - The new amount of the price.
   * @throws {TypeError} Throws an error if value is not a number.
   */
  set amount(value) {
    if (typeof value !== 'number') {
      throw new TypeError("Amount must be a number");
    }
    this._amount = value;
  }

  /**
   * Getter for the 'currency' attribute.
   * @returns {Currency} The currency of the price.
   */
  get currency() {
    return this._currency;
  }

  /**
   * Setter for the 'currency' attribute.
   * Ensures 'currency' is an instance of the Currency class.
   * @param {Currency} value - The new currency of the price.
   * @throws {TypeError} Throws an error if value is not a Currency instance.
   */
  set currency(value) {
    if (!(value instanceof Currency)) {
      throw new TypeError("Currency must be an instance of the Currency class");
    }
    this._currency = value;
  }

  /**
   * Method to display the full price in the format "amount currency_name (currency_code)".
   * @returns {string} The full price display.
   */
  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  /**
   * Static method to convert a price by a given conversion rate.
   * @param {number} amount - The amount to convert.
   * @param {number} conversionRate - The rate at which to convert the price.
   * @returns {number} The converted price.
   */
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
