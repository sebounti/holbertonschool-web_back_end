const updateStudentGradeByCity = (students, city, newGrades) => {
  if (!Array.isArray(students) || !Array.isArray(newGrades)) {
    return [];
  }
  const studentsByGrade = students
    .filter((student) => student.location === city)
    .map((student) => {
      const grades = newGrades.filter((note) => note.studentId === student.id);
      let grade = 'N/A';

      if (grades[0]) {
        grade = grades[0].grade;
      }

      return {
        ...student,
        grade,
      };
    });

  return studentsByGrade;
};

export default updateStudentGradeByCity;
