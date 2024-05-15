import { BrowserRouter as Router, Routes, Route } from "react-router-dom"; import './App.css';
import Home from './component/Home';
import DataTable from './component/DataTable'
import Error from './component/Error'

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/server" element={<DataTable />} />
          <Route path="/Error" element={<Error />}></Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
