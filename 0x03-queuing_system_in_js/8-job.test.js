import { expect } from "chai";
import createPushNotificationJobs from "./8-job";
import { createQueue } from "kue";

const queue = createQueue();

describe("test for createPushNotificationsJobs", () => {
  before(() => {
    queue.testMode.enter();
  });
  afterEach(() => {
    queue.testMode.clear();
  });
  after(() => {
    queue.testMode.exit();
  });

  it("add object to a queue", () => {
    queue.createJob("push_notif", { name: "jojo thomas" }).save();
    expect(queue.testMode.jobs.length).to.equal(1);
    queue.createJob("push_notif", { name: "joseph thomas" }).save();
    expect(queue.testMode.jobs.length).to.equal(2);
  });
  it("add object to a queue and check if content is correct", () => {
    queue.createJob("push_notif", { name: "jojo thomas" }).save();
    expect(queue.testMode.jobs[0].data).to.be.eql({ name: "jojo thomas" });
    queue.createJob("push_notif", { name: "joseph thomas" }).save();
    expect(queue.testMode.jobs[1].data).to.be.eql({ name: "joseph thomas" });
  });
});
