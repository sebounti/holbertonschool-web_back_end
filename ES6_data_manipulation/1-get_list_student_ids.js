const getListStudentIds = (ids) => {
  if (!Array.isArray(ids)) {
    return [];
  }
  const newArray = ids.map((item) => item.id);
  return newArray;
};

export default getListStudentIds;
