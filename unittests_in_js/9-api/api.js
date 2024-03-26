// task 8-api.js
const express = require("express");

const app = express();
const port = 7865;

app.get("/", (req, res) => {
  res.end("Welcome to the payment system");
});

app.get("/cart/:id(\\d+)", (req, res) => {
  const id = req.params.id;

  if (!/^\d+$/.test(id)) {
    return res.status(404).send("Not found");
  }

  res.send(`Payment methods for cart ${id}`);
});

// Gestion d'erreur "routes non trouvées"
app.use((req, res) => {
  res.status(404).send("Not Found");
});

// Gestion d'erreur "erreurs serveur"
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send("Something broke!");
});

app.listen(port, () => {
  console.log("API available on localhost port 7865");
});

module.exports = app;
