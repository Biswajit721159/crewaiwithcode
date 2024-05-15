import React, { useEffect, useState } from 'react'
import { ClipLoader } from 'react-spinners'
import FrontendBackend from './FrontendBackend'
import { useDispatch, useSelector } from 'react-redux'
import { codemethod } from '../Redux/CodeSlice'
import Code from './Code'
const Home = () => {
    const frontendcode = useSelector((state) => state?.code?.FrontendCode)
    const backendcode = useSelector((state) => state?.code?.BackendCode)

    let [loader, setloader] = useState(false)
    const dispatch = useDispatch();


    useEffect(() => {
        if (frontendcode?.length && backendcode?.length) {
            setloader(false)
        }
    }, [])

    function Submit() {
        setloader(true)
        fetch(`http://127.0.0.1:8000/api/pass`).then((resp) => resp.json())
            .then((result) => {
                setloader(false)
                dispatch(codemethod.Add_FrontendCode(result?.[0]?.FrontendCode))
                dispatch(codemethod.Add_BackendCode(result?.[1]?.BackendCode))
                // dispatch(codemethod.Add_FrontendcodeEditor(result?.[1]?.FrontendcodeEditor))
                // dispatch(codemethod.Add_BackendcodeEditor(result?.[3]?.BackendcodeEditor))
            }).catch((e) => {
                setloader(false)
                console.log(e)
            })
    }

    return (
        <>
            {loader === true ?
                <ClipLoader className='mx-5' color="black" size={'25px'} /> :
                <button type="button" onClick={Submit} className="btn btn-primary btn-sm mx-5  mt-1">Get Code</button>
            }
            {/* {loader === false && data.length != 0 && <Code data={data} />} */}
            {/* {loader === false && <FrontendBackend />} */}
            {loader === false && <Code />}
        </>
    )
}

export default Home