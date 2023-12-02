const express = require("express");
const fs = require("fs").promises;

const app = express();

function countStudents(path) {
  return fs.readFile(path, "utf8").then((fileContent) => {
    const lines = fileContent.split("\n").filter((line) => line.trim());
    lines.shift();

    const students = lines.map((line) => line.split(","));
    const fields = [...new Set(students.map((student) => student[3]))];

    let result = `Number of students: ${students.length}\n`;
    for (const field of fields) {
      const fieldStudents = students.filter((student) => student[3] === field);
      const fieldStudentsNames = fieldStudents.map((student) => student[0]);
      result += `Number of students in ${field}: ${
        fieldStudents.length
      }. List: ${fieldStudentsNames.join(", ")}\n`;
    }
    return result;
  });
}

app.get("/", (req, res) => {
  res.send("Hello Holberton School!");
});

app.get("/students", (req, res) => {
  countStudents(process.argv[2])
    .then((data) => {
      res.send(`This is the list of our students\n${data}`);
    })
    .catch(() => {
      res.status(500).send("Cannot load the database");
    });
});

app.listen(1245, () => {
  console.log("Server is running on port 1245");
});

module.exports = app;
