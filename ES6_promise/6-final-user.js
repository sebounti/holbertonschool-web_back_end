import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, filename) {
  return Promise.all([
    signUpUser(firstName, lastName),
    uploadPhoto(filename),
  ]).then((res) => {
    for (const x of res) {
      if (x.status === 'rejected') {
        x.value = `error: ${x.raison.message}`;
        delete x.raison;
      }
    }
    return res;
  });
}
