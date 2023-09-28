import { createClient } from "redis";

const client = createClient()
  .on("error", (error) => {
    console.log("Redis client not connected to the server: ", error.message);
  })
  .on("connect", () => {
    console.log("Redis client connected to the server");
  });

async function publishMessage(message, time) {
  await setTimeout(() => console.log(`About to send ${message}`), time);
  client.publish("holberton school channel", message, function (err, reply) {
    if (err) console.log(err);
  });
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
