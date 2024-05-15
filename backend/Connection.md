First, we need to install the mysql2 package. Open your terminal and navigate to your project directory, then run the following command:

```bash
npm install mysql2
```

Once the mysql2 package is installed, you can use the following code to connect to your MySQL database:

```javascript
const mysql = require('mysql2/promise');

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
```

You can now use this `connectToDatabase` function to connect to your MySQL database. It will return a Promise that resolves with the connection object, which can be used to execute queries on the database.

Please note that you need to handle the error and close the connection properly after using it.