// Import the ClassRoom class from the 0-classroom.js file
import ClassRoom from './0-classroom.js';

/**
 * Initializes and returns an array of ClassRoom objects with different sizes.
 * @returns {ClassRoom[]} Array of ClassRoom instances
 */
export default function initializeRooms() {
  return [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34)
  ];
}
