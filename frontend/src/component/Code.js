import React, { useState } from 'react'
import ConnectToDbCode from '../CodeSection/ConnectToDbCode'
import FetchDataFromDb from '../CodeSection/FetchDataFromDb'
import DisplayTable from '../CodeSection/DisplayTable'
import Frontendcode from '../CodeSection/Frontendcode'
import BackendCode from '../CodeSection/BackendCode'
const Code = () => {

    const [show1, setshow1] = useState(false)
    const [show2, setshow2] = useState(false)
    const [show3, setshow3] = useState(false)
    const [show4, setshow4] = useState(false)

    function ConnectToDataBaseOutput() {
        setshow1(true)
        setshow2(false)
        setshow3(false)
        setshow4(false)
    }

    function FetchDataFromDataBaseOutput() {
        setshow1(false)
        setshow2(true)
        setshow3(false)
        setshow4(false)
    }

    function DisplayItIntoTableOutput() {
        setshow1(false)
        setshow2(false)
        setshow3(true)
        setshow4(false)
    }

    function SummarizeOutput() {
        setshow1(false)
        setshow2(false)
        setshow3(false)
        setshow4(true)
    }

    function Hide() {
        setshow1(false)
        setshow2(false)
        setshow3(false)
        setshow4(false)
    }


    return (
        <>
            <button className='btn btn-info btn-sm mx-2' onClick={ConnectToDataBaseOutput}>Frontend Code</button>
            <button className='btn btn-info btn-sm mx-2' onClick={FetchDataFromDataBaseOutput}>Backend Code</button>
            {/* <button className='btn btn-info btn-sm mx-2' onClick={DisplayItIntoTableOutput}>Frontend Code Editor</button>
            <button className='btn btn-info btn-sm mx-2' onClick={SummarizeOutput}>Backend Code Editor</button> */}
            <button className='btn btn-info btn-sm mx-2' onClick={Hide}>Hide</button>
            <div className='code'>
                {show1 === true && <ConnectToDbCode />}
                {show2 === true && <FetchDataFromDb />}
                {/* {show3 === true && <Frontendcode />}
                {show4 === true && <BackendCode />} */}
            </div>
        </>
    )
}
export default Code