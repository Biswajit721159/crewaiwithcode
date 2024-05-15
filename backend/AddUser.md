Here is the React Functional component with Tailwind CSS for adding a user. The component makes a POST request to the '/users' endpoint which corresponds to the 'add user' API. 

```javascript
import React, { useState } from 'react';
import axios from 'axios';

const AddUserForm = () => {
    const [user, setUser] = useState({ full_name: '', email: '', mobile_number: '' });
    const [error, setError] = useState(null);

    const handleChange = e => {
        setUser({...user, [e.target.name]: e.target.value });
    }

    const handleSubmit = async e => {
        e.preventDefault();

        try {
            await axios.post('/users', user);
            setUser({ full_name: '', email: '', mobile_number: '' });
        } catch (err) {
            setError('An error occurred while adding the user.');
        }
    }

    return (
        <div className="container mx-auto px-4">
            <form onSubmit={handleSubmit} className="w-full max-w-sm mx-auto mt-5">
                <div className="mb-4">
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="full_name">
                        Full Name:
                    </label>
                    <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        name="full_name" type="text" value={user.full_name} onChange={handleChange} required />
                </div>

                <div className="mb-4">
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="email">
                        Email:
                    </label>
                    <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        name="email" type="email" value={user.email} onChange={handleChange} required />
                </div>

                <div className="mb-4">
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="mobile_number">
                        Mobile Number:
                    </label>
                    <input className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        name="mobile_number" type="text" value={user.mobile_number} onChange={handleChange} required />
                </div>

                {error && <p className="text-red-500 text-xs italic">{error}</p>}

                <div className="flex items-center justify-between">
                    <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                        type="submit">
                        Add User
                    </button>
                </div>
            </form>
        </div>
    );
}

export default AddUserForm;
```

To install the necessary packages, run the following commands:
- To install React: `npm install react`
- To install Axios for making API calls: `npm install axios`
- To install Tailwind CSS for styling: `npm install tailwindcss` 

Please replace '/users' with your actual API endpoint.