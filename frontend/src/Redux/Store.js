import { configureStore } from "@reduxjs/toolkit";
import codeReducer from '../Redux/CodeSlice'

export default configureStore({

  reducer: {
    code:codeReducer,
  },

});