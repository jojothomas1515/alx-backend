import { createClient } from "redis";

const client = createClient()
  .on("error", (error) => {
    console.log("Redis client not connected to the server: ", error.message);
  })
  .on("connect", () => {
    console.log("Redis client connected to the server");
  });

const fieldV = [
  "Portland=50",
  "Seattle=80",
  "New York=20",
  "Bogota=20",
  "Cali=40",
  "Paris=2",
];

fieldV.map((data) => {
  const [f, v] = data.split("=");
  client.hset("HolbertonSchools", f, v, (err, res) => {
    console.log(res);
  });
});

client.hgetall("HolbertonSchools", (err, data) => {
  if (err) console.log(err);
  console.log(data);
});
