import { createSlice } from "@reduxjs/toolkit";

const codeSlice = createSlice({
    name: "code",
    initialState: {
        FrontendCode: '',
        BackendCode: '',
        FrontendcodeEditor: '',
        BackendcodeEditor: ''
    },
    reducers: {
        Add_FrontendCode: (state, action) => {
            state.FrontendCode = action.payload
        },
        Add_BackendCode: (state, action) => {
            state.BackendCode = action.payload
        },
        Add_FrontendcodeEditor: (state, action) => {
            state.FrontendcodeEditor = action.payload
        },
        Add_BackendcodeEditor: (state, action) => {
            state.BackendcodeEditor = action.payload
        }
    },
});



export const codemethod = codeSlice.actions;
const codeReducer = codeSlice.reducer;
export default codeReducer;