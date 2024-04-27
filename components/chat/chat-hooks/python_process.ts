import express from 'express';
const { spawn } = require('child_process');
const app = express();
const port = 3000;

app.post('/api/add', (req, res) => {
    const a = parseInt(req.body.a);
    const b = parseInt(req.body.b);

    // 执行 Python 脚本并传递参数
    const pythonProcess = spawn('python', ['script.py', a, b]);

    let output = '';
    pythonProcess.stdout.on('data', (data) => {
        output += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
        res.status(500).send(data.toString());
    });

    pythonProcess.on('close', (code) => {
        if (code === 0) {
            res.send(output.trim());
        } else {
            res.status(500).send(`Python process exited with code ${code}`);
        }
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});