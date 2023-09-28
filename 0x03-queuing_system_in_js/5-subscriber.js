import { createClient } from "redis";

const client = createClient()
  .on("error", (error) => {
    console.log("Redis client not connected to the server: ", error.message);
  })
  .on("connect", () => {
    console.log("Redis client connected to the server");
  });

client.subscribe("holberton school channel", function (err, res) {
  if (err) {
    console.log(err);
  }
  console.log("Connected to :", res);
});

client.on("message", function (chan, msg) {
  if (chan === "holberton school channel") {
    if (msg === "KILL_SERVER")
      client.UNSUBSCRIBE("holberton school channel", function (err, reply) {
        if (err) {
          console.log(err);
        } else {
          console.log("UNSUBBED from :", reply);
        }
      });
    console.log(msg);
  }
});
