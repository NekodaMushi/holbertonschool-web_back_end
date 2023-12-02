export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const gradEl = newGrades.find((el) => el.studentId === student.id);

      const updatedStudent = student;
      if (gradEl) {
        updatedStudent.grade = gradEl.grade;
      } else {
        updatedStudent.grade = 'N/A';
      }
      return updatedStudent;
    });
}
