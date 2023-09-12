function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  // Creates a 'budget' object with keys calculated using the year
  // actual year.
  // The keys are created using string templates of
  // characters (` `) to incorporate the current
  // the actual year in the name of each key.
  const budget = {

  [`income-${getCurrentYear()}`]:income,
  [`gdp-${getCurrentYear()}`]: gdp,
  [`capita-${getCurrentYear()}`]: capita,
  };
  return budget;
}
