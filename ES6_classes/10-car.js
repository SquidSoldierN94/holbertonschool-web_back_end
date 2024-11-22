export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const clonedCar = Object.create(Object.getPrototypeOf(this));
    clonedCar._brand = this._brand;
    clonedCar._motor = this._motor;
    clonedCar._color = this._color;
    return clonedCar;
  }
}
