/**
 * Class representing a building.
 * This class is considered abstract, and any class extending it must implement 
 * the 'evacuationWarningMessage' method.
 */
export default class Building {
    /**
     * Create a new Building instance.
     * @param {number} sqft - The square footage of the building.
     */
    constructor(sqft) {
      if (this.constructor !== Building && typeof this.evacuationWarningMessage !== 'function') {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
      this._sqft = sqft;
    }
  
    /**
     * Getter for the 'sqft' attribute.
     * @returns {number} The square footage of the building.
     */
    get sqft() {
      return this._sqft;
    }
  }
  