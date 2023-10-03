const getStudentsByLocation = (students, city) => {
  const studentsByLocation = students.filter(
    (student) => student.location === city,
  );

  return studentsByLocation;
};

export default getStudentsByLocation;
