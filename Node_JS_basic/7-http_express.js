const express = require('express');
const fs = require('fs');

const app = express();

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const lines = data.split('\n').filter((line) => line.trim() !== '');
        const students = lines.slice(1).map((line) => line.split(','));
        const totalStudents = students.length;

        const fields = {};
        students.forEach(([firstname, lastname, age, field]) => {
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        });

        let output = `Number of students: ${totalStudents}`;
        for (const [field, names] of Object.entries(fields)) {
          output += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
        }
        resolve(output);
      }
    });
  });
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const databasePath = process.argv[2];
  if (!databasePath) {
    res.status(500).send('Database file path is not provided');
    return;
  }

  res.write('This is the list of our students\n');
  countStudents(databasePath)
    .then((output) => {
      res.end(output);
    })
    .catch((err) => {
      res.end(err.message);
    });
});

app.listen(1245);

module.exports = app;
