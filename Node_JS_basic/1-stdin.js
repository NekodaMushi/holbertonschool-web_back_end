console.log("Welcome to Holberton School, what is your name?");

process.stdin.on("readable", () => {
  let name = process.stdin.read();
  if (name !== null) {
    name = name.toString().trim();
    process.stdout.write(`Your name is: ${name}\n`);
  }
});

process.stdin.on("end", () => {
  process.stdout.write("This important software is now closing\n");
  process.exit();
});
