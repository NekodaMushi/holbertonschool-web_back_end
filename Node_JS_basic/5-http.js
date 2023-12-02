const http = require('http');
const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf8').then((fileContent) => {
    const lines = fileContent.split('\n').filter((line) => line.trim());
    lines.shift();

    const students = lines.map((line) => line.split(','));
    const fields = [...new Set(students.map((student) => student[3]))];

    let result = `Number of students: ${students.length}\n`;
    for (const field of fields) {
      const fieldStudents = students.filter((student) => student[3] === field);
      const fieldStudentsNames = fieldStudents.map((student) => student[0]);
      result += `Number of students in ${field}: ${
        fieldStudents.length
      }. List: ${fieldStudentsNames.join(', ')}\n`;
    }
    return result;
  });
}

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    countStudents(process.argv[2])
      .then((data) => {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(`This is the list of our students\n${data}`);
      })
      .catch(() => {
        res.writeHead(500);
        res.end('Cannot load the database');
      });
  }
});

app.listen(1245);

module.exports = app;
