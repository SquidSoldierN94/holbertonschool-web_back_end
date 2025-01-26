const http = require('http');
const url = require('url');
const { readFile } = require('fs');
const path = require('path');

const countStudents = (filePath) => {
  return new Promise((resolve, reject) => {
    readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const lines = data.split('\n').filter((line) => line.trim() !== '');
        const students = lines.slice(1);
        const fields = {};

        students.forEach((student) => {
          const [name, , , field] = student.split(',');
          if (!fields[field]) fields[field] = [];
          fields[field].push(name);
        });

        const output = [`Number of students: ${students.length}`];
        for (const field in fields) {
          output.push(
            `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`
          );
        }
        resolve(output.join('\n'));
      }
    });
  });
};

const app = http.createServer(async (req, res) => {
  const parsedUrl = url.parse(req.url, true);
  const filePath = path.resolve(process.argv[2]);

  if (parsedUrl.pathname === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (parsedUrl.pathname === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');

    try {
      const studentsData = await countStudents(filePath);
      res.end(studentsData);
    } catch (err) {
      res.end(err.message);
    }
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
