// Cette fonction retourne l'année actuelle.
function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

// Cette fonction crée un objet 'budget' avec des clés calculées en utilisant
// l'année actuelle.
// Les clés sont créées en utilisant des templates de chaînes de caractères
//(` `) pour incorporer
// l'année actuelle dans le nom de chaque clé. Les valeurs 'income',
//'gdp', et 'capita' sont
// associées aux clés correspondantes.
export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {
    [`income-${getCurrentYear()}`]: income,
    [`gdp-${getCurrentYear()}`]: gdp,
    [`capita-${getCurrentYear()}`]: capita,
  };

  return budget;
}
