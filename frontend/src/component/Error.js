import React from 'react';
import { useLocation } from 'react-router-dom';
import { Link } from 'react-router-dom';

const NotFound = () => {
    const location = useLocation();
    const { data } = location?.state;
    return (
        <div className="container text-center mt-5">
            <p>Note : First it is run the backend code then only it is run the frontend code</p>
            <h1 className="display-1">404</h1>
            {typeof (data) !== 'object' ? <p className="lead" style={{ color: 'red' }}>Your error message is - {data} </p>:
            <p className="lead" style={{ color: 'red' }}>Page Not Found !</p>}
            <Link to="/" className="btn btn-primary">Go to Home</Link>
        </div>
    );
}

export default NotFound;
