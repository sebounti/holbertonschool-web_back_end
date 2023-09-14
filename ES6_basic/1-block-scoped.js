// 1-block-scoped.js
/* eslint-disable no-unused-vars */
export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    // eslint-disable-next-line no-unused-vars
    const task = true;
    const task2 = false;
  }

  return [task, task2];
}
