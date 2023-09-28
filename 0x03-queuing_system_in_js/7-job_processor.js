import { createQueue } from "kue";

const blackList = ["4153518780", "4153518781"];
const queue = createQueue();

function sendNotification(phoneNumber, message, job, done) {
  if (phoneNumber === blackList[1] || phoneNumber === blackList[0])
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));

  console.log(`Sending notification to ${phoneNumber}, with message: ${message}
`);

  job.progress(0, 100);
  job.progress(50, 100);
}

queue.process("push_notification_code_2", 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
  done();
});
