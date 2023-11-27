export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const gradEl = newGrades.find((el) => el.studentId === student.id);

      if (gradEl) {
        student.grade = gradEl.grade;
      } else {
        student.grade = "N/A";
      }
      return student;
    });
}
