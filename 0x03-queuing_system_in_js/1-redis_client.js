import { createClient } from "redis";

const client = createClient()
  .on("error", (error) => {
    console.log("Redis client not connected to the server: ", error.message);
  })
  .on("connect", () => console.log("Redis client connected to the server"));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, res) => {
    console.log("Reply: " + res);
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, res) => {
    console.log(res);
  });
}
displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
