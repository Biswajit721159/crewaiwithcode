Below is the React.js code for displaying users in a table format. This code uses functional components, hooks for managing state and side effects, and Tailwind CSS for styling.

```javascript
import React, { useState, useEffect } from 'react';

// Importing Axios to make HTTP requests
import axios from 'axios';

// Importing react-router-dom to use Link component
import { Link } from 'react-router-dom';

const Users = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const res = await axios.get('api_endpoint_for_users');
        setUsers(res.data);
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    };

    fetchUsers();
  }, []);

  const deleteUser = async (id) => {
    try {
      await axios.delete(`api_endpoint_for_deleting_user/${id}`);
      setUsers(users.filter(user => user.id !== id));
    } catch (error) {
      console.error('Error deleting user:', error);
    }
  };

  return (
    <div className="container mx-auto px-4">
      <h2 className="text-2xl font-semibold mb-4">Users</h2>
      <table className="w-full border">
        <thead>
          <tr>
            <th className="border px-4 py-2">ID</th>
            <th className="border px-4 py-2">Full Name</th>
            <th className="border px-4 py-2">Mobile Number</th>
            <th className="border px-4 py-2">Email</th>
            <th className="border px-4 py-2">Actions</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.id}>
              <td className="border px-4 py-2">{user.id}</td>
              <td className="border px-4 py-2">{user.full_name}</td>
              <td className="border px-4 py-2">{user.mobile_number}</td>
              <td className="border px-4 py-2">{user.email}</td>
              <td className="border px-4 py-2">
                <Link to={`/update/${user.id}`} className="text-blue-500">Update</Link>
                <button onClick={() => deleteUser(user.id)} className="text-red-500 ml-4">Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Users;
```

Please replace the `api_endpoint_for_users` with your actual API endpoint for getting all users and `api_endpoint_for_deleting_user` with your actual API endpoint for deleting a user. The delete function removes the user from the state immediately for a better user experience. However, if the delete request fails, you might want to handle that and possibly add the user back to the state or show an error message.