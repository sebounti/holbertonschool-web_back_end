/* 0_promise.js */
export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const condition = true;
    if (condition) {
      resolve('true');
    } else {
      reject(new Error('false error message'));
    }
  });
}
