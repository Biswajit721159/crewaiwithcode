import React, { useState } from 'react'
import Frontendcode from '../CodeSection/Frontendcode'
import BackendCode from '../CodeSection/BackendCode'
import Error from '../component/Error'
import DataTable from '../component/DataTable'
import { useSelector } from 'react-redux'
import { useNavigate } from 'react-router-dom'

const api = process.env.REACT_APP_API

const FrontendBackend = () => {
    const [show1, setshow1] = useState(false)
    const [show2, setshow2] = useState(false)
    const [run, setrun] = useState("Run Code")
    const [disable, setdisable] = useState(false)
    const history = useNavigate()

    function Frontend() {
        setshow2(false)
        setshow1(true)
    }

    function Backend() {
        setshow1(false)
        setshow2(true)
    }

    function Hide() {
        setshow1(false)
        setshow2(false)
    }

    let frontendcode = useSelector((state) => state?.code?.FrontendCode)
    let backendcode = useSelector((state) => state?.code?.BackendCode)
    const [dynamicComponent, setDynamicComponent] = useState(null);
    const [data, setData] = useState([])

    function RunCode() {
        setrun("Runing .....")
        setdisable(true)

        fetch(`${api}/code`, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                code: backendcode
            })
        }).then((res) => res.json())
            .then((data) => {
                setrun("Run Code");
                setdisable(false);

                if (Array.isArray(data)) {
                    
                    // console.log("came")
                    // window.eval(frontendcode);
                    // console.log("came end")
                    // const component = window['DynamicComponent'];
                    // console.log('Dynamically created component:', component);
                    // if (component) {
                    //     setDynamicComponent(component);
                    //     setData(data);
                    // } else {
                    //     console.error('Dynamic component not defined.');
                    // }

                    history('/server', { state: { data: data } });
                }
                else {
                    history('/Error', { state: { data: data } });
                }
            }).catch((error) => {
                console.log("error is ", error)
                setrun("Run Code");
                setdisable(false);
                history('/Error', { state: { data: error } });
            })
    }


    return (
        <>
            <button className="btn btn-info btn-sm mx-2 mt-1" onClick={Frontend}>Frontend code</button>
            <button className="btn btn-info btn-sm mx-2 mt-1" onClick={Backend}>Backend code</button>
            <button className="btn btn-info btn-sm mx-2 mt-1" onClick={Hide}>Hide</button>
            <button className='btn btn-danger btn-sm mx-5 mt-1' disabled={disable} onClick={RunCode}>{run}</button>
            <div className='code'>
                {show1 === true && <Frontendcode />}
                {show2 === true && <BackendCode />}
            </div>
            {dynamicComponent && React.createElement(dynamicComponent, { ...data })} 
        </>
    )
}

export default FrontendBackend