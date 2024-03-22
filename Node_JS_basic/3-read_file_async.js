const fs = require('fs');

async function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .split('\n')
        .filter(Boolean)
        .slice(1)
        .map((line) => {
          const [firstname, lastname, age, field] = line.split(',');
          return {
            firstname,
            lastname,
            age,
            field,
          };
        });

      const cs = lines.filter((student) => student.field === 'CS');
      const swe = lines.filter((student) => student.field === 'SWE');

      console.log(`Number of students: ${lines.length}`);
      console.log(
        `Number of students in CS: ${cs.length}. List: ${cs
          .map((student) => student.firstname)
          .join(', ')}`,
      );
      console.log(
        `Number of students in SWE: ${swe.length}. List: ${swe
          .map((student) => student.firstname)
          .join(', ')}`,
      );
      resolve();
    });
  });
}
module.exports = countStudents;
