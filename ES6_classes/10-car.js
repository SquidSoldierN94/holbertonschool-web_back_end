/**
 * Class representing a Car.
 */
export default class Car {
    /**
     * Create a new Car instance.
     * @param {string} brand - The brand of the car.
     * @param {string} motor - The motor type of the car.
     * @param {string} color - The color of the car.
     */
    constructor(brand, motor, color) {
      this._brand = brand;
      this._motor = motor;
      this._color = color;
    }
  
    /**
     * Clone the current car by creating a new instance with the same properties.
     * @returns {Car} A new Car instance with the same attributes.
     */
    cloneCar() {
      const clonedCar = Object.create(Object.getPrototypeOf(this));
      clonedCar._brand = this._brand;
      clonedCar._motor = this._motor;
      clonedCar._color = this._color;
      return clonedCar;
    }
  }
  