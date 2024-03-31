// 0-redis_client.js
import { createClient, print } from "redis";

const client = createClient();

client.on("connect", () => {
  console.log("Le client Redis est connecté au serveur");
});

client.on("error", (err) => {
  console.log(`Le client Redis n'est pas connecté au serveur : ${err.message}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, res) => {
    console.log(res);
  });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
