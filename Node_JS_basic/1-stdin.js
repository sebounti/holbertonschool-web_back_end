process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('readable', () => {
  const resp = process.stdin.read();

  if (resp) {
    process.stdout.write(`Your name is: ${resp}`);
  }
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
