// task 6-payement_token.js
function getPaymentTokenFromAPI(success) {
  return new Promise((resolve) => {
    if (success) {
      resolve({ data: "Successful response from the API" });
    }
  });
}

module.exports = getPaymentTokenFromAPI;
