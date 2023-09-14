export default class HolbertonCourse {
// constructor(name, lenght, student)
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._student = students;
  }

  // getter and setter name
  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  // getter and setter lenght
  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = value;
  }

  // getter and setter student
  get students() {
    return this._students;
  }

  set students(studentvalue) {
    if (!studentsvalue.every((student) => typeof student === 'string')) {
      throw new TypeError('Student must be an object');
    }
    this._students = studentvalue;
  }
}
