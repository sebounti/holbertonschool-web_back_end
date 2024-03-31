// task 6 - Create the Job creator
const kue = require("kue");
const queue = kue.createQueue();

const jobData = {
  phoneNumber: "0645678900",
  message: "This is the code to verify your account",
};

const nameQueue = "push_notification_code";

const job = queue.create(nameQueue, jobData).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on("complete", () => {
  console.log(`Notification job completed`);
});

job.on("failed", () => {
  console.log(`Notification job failed`);
});
