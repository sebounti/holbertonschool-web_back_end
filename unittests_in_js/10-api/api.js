const express = require("express");

const app = express();
const port = 7865;

// middleware
app.use(express.json());

app.get("/", (req, res) => {
  res.end("Welcome to the payment system");
});

app.get("/cart/:id(\\d+)", (req, res) => {
  const id = req.params.id;
  res.send(`Payment methods for cart ${id}`);
});

app.get("/available_payments", (req, res) => {
  const payment_methods = {
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  };
  res.json(payment_methods);
});

app.post("/login", (req, res) => {
  const userName = req.body.userName;
  if (userName) {
    res.send(`Welcome ${userName}`);
  } else {
    res.status(400).send(`Username is required`);
  }
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

// Démarrez le serveur
app
  .listen(port, () => {
    console.log(`API available on localhost port ${port}`);
    console.log(`Server listening at http://localhost:${port}`);
  })
  .on("error", (err) => {
    console.error("Error starting server:", err);
  });
