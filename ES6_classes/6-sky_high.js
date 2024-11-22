import Building from './5-building.js';

/**
 * Class representing a SkyHighBuilding, which is a subclass of Building.
 */
export default class SkyHighBuilding extends Building {
  /**
   * Create a new SkyHighBuilding instance.
   * @param {number} sqft - The square footage of the building.
   * @param {number} floors - The number of floors in the building.
   */
  constructor(sqft, floors) {
    super(sqft); // Call the parent class constructor to initialize sqft
    this._floors = floors; // Initialize the floors attribute
  }

  /**
   * Getter for the 'floors' attribute.
   * @returns {number} The number of floors in the building.
   */
  get floors() {
    return this._floors;
  }

  /**
   * Override the 'evacuationWarningMessage' method from the parent class.
   * @returns {string} The evacuation warning message.
   */
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
