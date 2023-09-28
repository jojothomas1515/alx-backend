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
    createPushNotificationJobs([{ name: "jojo thomas" }], queue);
    expect(queue.testMode.jobs.length).to.equal(1);
    createPushNotificationJobs([{ name: "joseph thomas" }], queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });
  it("add object to a queue and check if content is correct", () => {
    createPushNotificationJobs([{ name: "jojo thomas" }], queue);
    expect(queue.testMode.jobs[0].data).to.be.eql({ name: "jojo thomas" });
    createPushNotificationJobs([{ name: "joseph thomas" }], queue);
    expect(queue.testMode.jobs[1].data).to.be.eql({ name: "joseph thomas" });
  });
});
