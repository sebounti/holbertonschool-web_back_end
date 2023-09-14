class HolbertonCourse {
  constructor(name, lenght, student) {
    this._name = name;
    this._lenght = lenght;
    this._student = student;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  get lenght() {
    return this._lenght;
  }

  set lenght(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Lenght must be a number');
    }
    this._lenght = value;
  }

  get student() {
    return this._student;
  }

  set student(value) {
    if (typeof value !== 'object') {
      throw new TypeError('Student must be an object');
    }
    this._student = value;
  }
}
