// 2-hbtn_course.js

/**
 * Class representing a Holberton Course.
 */
export default class HolbertonCourse {
    /**
     * Create a new HolbertonCourse instance.
     * @param {string} name - The name of the course.
     * @param {number} length - The length of the course in weeks.
     * @param {array} students - An array of student names.
     */
    constructor(name, length, students) {
      this._name = name;
      this._length = length;
      this._students = students;
  
      this.name = name;
      this.length = length;
      this.students = students;
    }
  
    /**
     * Getter for the 'name' attribute.
     * @returns {string} The name of the course.
     */
    get name() {
      return this._name;
    }
  
    /**
     * Setter for the 'name' attribute.
     * Ensures 'name' is a string.
     * @param {string} value - The new name of the course.
     * @throws {TypeError} Throws an error if value is not a string.
     */
    set name(value) {
      if (typeof value !== 'string') {
        throw new TypeError("Name must be a string");
      }
      this._name = value;
    }
  
    /**
     * Getter for the 'length' attribute.
     * @returns {number} The length of the course.
     */
    get length() {
      return this._length;
    }
  
    /**
     * Setter for the 'length' attribute.
     * Ensures 'length' is a number.
     * @param {number} value - The new length of the course.
     * @throws {TypeError} Throws an error if value is not a number.
     */
    set length(value) {
      if (typeof value !== 'number') {
        throw new TypeError("Length must be a number");
      }
      this._length = value;
    }
  
    /**
     * Getter for the 'students' attribute.
     * @returns {array} The list of students in the course.
     */
    get students() {
      return this._students;
    }
  
    /**
     * Setter for the 'students' attribute.
     * Ensures 'students' is an array of strings.
     * @param {array} value - The new list of students.
     * @throws {TypeError} Throws an error if value is not an array of strings.
     */
    set students(value) {
      if (!Array.isArray(value) || !value.every(student => typeof student === 'string')) {
        throw new TypeError("Students must be an array of strings");
      }
      this._students = value;
    }
  }
