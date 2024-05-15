import React, { useEffect, useRef } from 'react';
import Prism from 'prismjs';
import 'prismjs/themes/prism.css';
import '../App.css'
import { useSelector } from 'react-redux';
const FetchDataFromDb = (message) => {

    message = useSelector((state) => state?.code?.BackendCode)
    const codeRef = useRef(null);


    return (
        <>
            {message && Array.isArray(message) ? message.map((ele, index) => (
                <div className='chat bot mt-3' key={index}>
                    <div >
                        {ele.code !== undefined ?
                            <div className='txt'>
                                <pre ref={codeRef} className='codecopy txt' style={{ backgroundColor: '#FBFCFC' }}>
                                    <code className="txt language-cpp" >
                                        {ele.code}
                                    </code>
                                </pre>
                            </div>
                            : (
                                <pre className='txt' style={{ whiteSpace: 'wrap' }} >{ele.text}</pre>
                            )}
                    </div>
                </div>
            )) : <pre>{message}</pre>}
        </>
    );
};


export default FetchDataFromDb;

