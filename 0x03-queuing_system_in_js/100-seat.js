import { createClient } from "redis";
import { promisify } from "util";
import { Job, createQueue } from "kue";
import express from "express";
import http from "http";

const client = createClient();
const gets = promisify(client.get).bind(client);
const sets = promisify(client.set).bind(client);
let reservationEnabled = true;

client.on("connect", () => {
  console.log("Connected to redis successfully");
});

function reserveSeat(number) {
  client.set("available_seats", number, function (err, reply) {
    console.log("Seats reserved");
  });
}

async function getCurrentAvailableSeats() {
  return await gets("available_seats");
}

reserveSeat(50);
const queue = createQueue();
const app = express();

app.get("/available_seats", async function (req, res) {
  const seats = await getCurrentAvailableSeats();
  return res.json({ numberOfAvailableSeats: seats });
});

app.get("/reserve_seat", function (req, res) {
  if (!reservationEnabled)
    return res.json({ status: "Reservation are blocked" });
  const job = queue
    .createJob("reserve_seat", { seats: 1 })
    .save(function (err) {
      if (err) return res.json({ status: "Reservation failed" });
    });

  job.on("complete", function () {
    console.log(`Seat reservation job ${job.id} completed`);
  });
  job.on("failed", function (err) {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
  return res.json({ status: "Reservation in process" });
});

app.get("/process", function (req, res) {
  queue.process("reserve_seat", async function (job, done) {
    const seats = await getCurrentAvailableSeats();
    const aSeats = Number(seats) - 1;
    if (aSeats >= 0) {
      if (aSeats == 0) reservationEnabled = false;
      reserveSeat(aSeats);
      done();
    }
    done(new Error("Not enough seats available"));
  });

  return res.json({ status: "Queue processing" });
});

const server = http.createServer(app);
const PORT = 1245;
server.listen(PORT, function () {
  console.log("listening on port", PORT);
});
