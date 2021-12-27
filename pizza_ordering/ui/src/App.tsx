import { Route, Routes } from 'react-router-dom';
import { Footer } from './components/Footer/Footer';
import { Menu } from './components/Menu/Menu';
import { Navbar } from './components/Navbar/Navbar';
import { Orders } from './components/Orders/Orders';


function App() {
  return (
    <div className="App">
      <Navbar />      
      <Routes>
        <Route path="/" element={<Menu />} /> 
        <Route path="order" element={<Orders />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
