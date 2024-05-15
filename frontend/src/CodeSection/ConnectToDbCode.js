import React, { useEffect, useRef, useState } from 'react';
import MonacoEditor from 'react-monaco-editor';
import '../App.css'
import { useSelector } from 'react-redux';
const ConnectToDbCode = (message) => {

    message = useSelector((state) => state?.code?.FrontendCode)
    const codeRef = useRef(null);

    const [code, setCode] = useState('');

    const handleChange = (newCode) => {
        setCode(newCode);
    };



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


export default ConnectToDbCode;

