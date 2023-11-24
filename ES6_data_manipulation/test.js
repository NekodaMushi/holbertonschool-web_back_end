const array = [
  { id: 1, firstName: "Guillaume", location: "San Francisco" },
  { id: 2, firstName: "James", location: "Columbia" },
  { id: 5, firstName: "Serena", location: "San Francisco" },
];

import getListStudents from "./0-get_list_students.js";

function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.city === city);
  // .map((student) => {
  //   const gradEl = newGrades.find(grade => grade.);
  // });
}

console.log(
  updateStudentGradeByCity(getListStudents(), "San Francisco", [
    { studentId: 5, grade: 97 },
    { studentId: 1, grade: 86 },
  ])
);

console.log(
  updateStudentGradeByCity(getListStudents(), "San Francisco", [
    { studentId: 5, grade: 97 },
  ])
);
