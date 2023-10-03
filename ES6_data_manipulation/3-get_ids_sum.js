const getStudentIdsSum = (students) => {
  const all = students
    .map((student) => student.id)
    .reduce((prev, curr) => prev + curr, 0);

  return all;
};

export default getStudentIdsSum;
