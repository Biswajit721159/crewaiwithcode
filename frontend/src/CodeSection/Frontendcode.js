import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { codemethod } from '../Redux/CodeSlice';
import Editor from "@monaco-editor/react";
const Frontendcode = () => {

    let data = useSelector((state) => state?.code?.FrontendcodeEditor)
    const dispatch = useDispatch();
    
    const [code, setCode] = useState(data);

    const handleChange = (newCode) => {
        setCode(newCode);
        dispatch(codemethod.Add_FrontendCode(newCode))
    };

    return (
        <>
            <div style={{ width: '100%' }}>
                <h4 style={{ textAlign: 'center', marginTop: '40px' }}>Frontend code editor</h4>
                <div>
                    <Editor
                        height="600px"
                        language="javascript"
                        theme="vs-dark"
                        value={code}
                        onChange={handleChange}
                        options={{
                            inlineSuggest: true,
                            fontSize: "14px",
                            formatOnType: true,
                            autoClosingBrackets: true,
                            minimap: { scale: 10 }
                        }}
                    />
                </div>
            </div>
        </>
    )
}
export default Frontendcode