Here is the complete App.js code for your React.js application.

```javascript
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Users from './Users';
import AddUserForm from './AddUserForm';
import UpdateUserForm from './UpdateUserForm';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Users />} />
        <Route path="/add" element={<AddUserForm />} />
        <Route path="/update/:id" element={<UpdateUserForm />} />
      </Routes>
    </Router>
  );
}

export default App;
```

In the above code, `BrowserRouter` is being used as the router. The `Routes` component is a container for `Route` components, and `Route` is used to define the mapping between the URL path and the component that should be rendered.

Users component will render when the URL is "/", AddUserForm will render when the URL is "/add", and UpdateUserForm will render when the URL is "/update/:id".

Please replace `./Users`, `./AddUserForm`, and `./UpdateUserForm` with the actual path of your components.

To install react-router-dom, run the command `npm install react-router-dom@6`.

This App.js follows the latest conventions of react-router-dom v6, where `Routes` is used instead of `Switch` and `element` is used instead of `component`. It also uses 'react-router-dom's' dynamic route matching ("/update/:id") to pass the id parameter to the UpdateUserForm component.