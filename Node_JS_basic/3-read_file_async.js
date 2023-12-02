const fs = require('fs').promises;

function countStudents(path) {
  return fs
    .readFile(path, 'utf8')
    .then((fileContent) => {
      const lines = fileContent.split('\n').filter((line) => line.trim());

      lines.shift();

      const students = lines.map((line) => line.split(','));

      const fields = [...new Set(students.map((student) => student[3]))];

      console.log(`Number of students: ${students.length}`);

      for (const field of fields) {
        const fieldStudents = students.filter(
          (student) => student[3] === field,
        );
        const fieldStudentsNames = fieldStudents.map((student) => student[0]);
        console.log(
          `Number of students in ${field}: ${
            fieldStudents.length
          }. List: ${fieldStudentsNames.join(', ')}`,
        );
      }
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
