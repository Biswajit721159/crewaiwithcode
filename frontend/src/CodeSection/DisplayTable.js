import React, { useEffect, useRef } from 'react';
import Prism from 'prismjs';
import 'prismjs/themes/prism.css';
import '../App.css'
const DisplayTable = (message) => {

    message = message.data
    const codeRef = useRef(null);

    useEffect(() => {
        Prism.highlightAll();
    }, []);



    return (
        <>
            {message && Array.isArray(message) ? message.map((ele, index) => (
                <div className='chat bot' key={index}>
                    <div >
                        {ele.code !== undefined ?
                            <div className='txt'>
                                <pre ref={codeRef} className='codecopy txt' style={{ backgroundColor: '#FBFCFC' }}>
                                    <code className="txt language-cpp">
                                        {ele.code}
                                    </code>
                                </pre>
                            </div>
                            : (
                                <pre className='txt' style={{ whiteSpace: 'wrap' }}>{ele.text}</pre>
                            )}
                    </div>
                </div>
            )) : <pre>{message}</pre>}
        </>
    );
};

export default DisplayTable;

