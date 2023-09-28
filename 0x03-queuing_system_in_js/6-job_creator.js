import { createQueue } from "kue";
import { createClient } from "redis";

const queue = createQueue();
const data = {
  phoneNumber: "00899392384",
  message: "Baba black sheep have you any wool",
};
const job = queue
  .create("push_notification_code", data)
  .save(function (err, res) {
    if (!err) console.log("Notification job created:", job.id);
  });

job.on("complete", function (res) {
  console.log("Notification job completed");
});
job.on("failed", function (err) {
  console.log("Notification job failed");
});
