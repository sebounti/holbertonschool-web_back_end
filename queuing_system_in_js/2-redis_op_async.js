// 0-redis_client.js
import { createClient, print } from "redis";
import { promisify } from "util";

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

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const res = await getAsync(schoolName);
    console.log(res);
  } catch (err) {
    console.error(err);
  }
}

(async () => {
  await displaySchoolValue("Holberton");
  setNewSchool("HolbertonSanFrancisco", "100");
  await displaySchoolValue("HolbertonSanFrancisco");
})();
