// task 5-subscriber.js
import redis from "redis";

const subscriber = redis.createClient();

subscriber.on("connect", () => {
  console.log("Redis client connected to the server");
});

subscriber.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const Channel = "holberton school channel";

subscriber.subscribe(Channel);

subscriber.on("message", (channel, message) => {
  if (channel === Channel) console.log(message);

  if (message === "KILL_SERVER") {
    subscriber.unsubscribe(Channel);
    subscriber.quit();
  }
});
