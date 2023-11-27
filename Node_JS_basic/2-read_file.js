const fs = require("fs");

function countStudents(path) {
  // Check if the file exists
  if (!fs.existsSync(path)) {
    throw new Error("Cannot load the database");
  }

  const fileContent = fs.readFileSync(path, "utf8");

  const lines = fileContent.split("\n").filter((line) => line.trim());

  // Remove the header
  lines.shift();

  // Parsing the CSV data
  const students = lines.map((line) => line.split(","));

  const fields = [...new Set(students.map((student) => student[3]))];
  console.log(`Number of students: ${students.length}`);

  for (const field of fields) {
    const fieldStudents = students.filter((student) => student[3] === field);
    const fieldStudentsNames = fieldStudents.map((student) => student[0]);
    console.log(
      `Number of students in ${field}: ${
        fieldStudents.length
      }. List: ${fieldStudentsNames.join(", ")}`
    );
  }
}

module.exports = countStudents;
