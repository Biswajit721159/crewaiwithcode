Here is my best complete final answer to the task:

```javascript
const express = require('express');
const cors = require('cors');
const mysql = require('mysql2/promise');

const app = express();
app.use(cors());
app.use(express.json());

async function connectToDatabase() {
    try {
        const connection = await mysql.createConnection({
            host: 'localhost',
            user: 'root',
            password: '190183',
            database: 'Users'
        });

        console.log('Connected to the MySQL server.');
        return connection;
        
    } catch (error) {
        console.error('Error connecting to the MySQL server:', error);
        throw error;
    }
}

app.get('/users', async (req, res) => {
    try {
        const connection = await connectToDatabase();
        const [rows] = await connection.query('SELECT * FROM $users');
        res.json(rows);
        await connection.end();
    } catch (error) {
        console.error(`Error: ${error}`);
        res.status(500).send('An error occurred while retrieving users.');
    }
});

app.get('/users/:id', async (req, res) => {
    try {
        const connection = await connectToDatabase();
        const [rows] = await connection.query('SELECT * FROM $users WHERE $id = ?', [req.params.id]);
        res.json(rows[0]);
        await connection.end();
    } catch (error) {
        console.error(`Error: ${error}`);
        res.status(500).send('An error occurred while retrieving the user.');
    }
});

app.post('/users', async (req, res) => {
    try {
        const connection = await connectToDatabase();
        const { full_name, mobile_number, email } = req.body;
        const [result] = await connection.query('INSERT INTO $users (full_name, mobile_number, email) VALUES (?, ?, ?)', [full_name, mobile_number, email]);
        res.status(201).send({ id: result.insertId });
        await connection.end();
    } catch (error) {
        console.error(`Error: ${error}`);
        res.status(500).send('An error occurred while adding the user.');
    }
});

app.put('/users/:id', async (req, res) => {
    try {
        const connection = await connectToDatabase();
        const { full_name, mobile_number, email } = req.body;
        await connection.query('UPDATE $users SET full_name = ?, mobile_number = ?, email = ? WHERE $id = ?', [full_name, mobile_number, email, req.params.id]);
        res.send({ message: 'User updated successfully' });
        await connection.end();
    } catch (error) {
        console.error(`Error: ${error}`);
        res.status(500).send('An error occurred while updating the user.');
    }
});

app.delete('/users/:id', async (req, res) => {
    try {
        const connection = await connectToDatabase();
        await connection.query('DELETE FROM $users WHERE $id = ?', [req.params.id]);
        res.send({ message: 'User deleted successfully' });
        await connection.end();
    } catch (error) {
        console.error(`Error: ${error}`);
        res.status(500).send('An error occurred while deleting the user.');
    }
});

app.listen(5000, () => console.log('Server is running on port 5000'));
```

Please replace `$users` and `$id` with your actual table name and id field name. This code includes all the necessary CRUD operations on the users table. It also handles errors properly and ensures the database connection is closed after each operation.

Remember to run your application with the command `node app.js` (or whatever your filename is).