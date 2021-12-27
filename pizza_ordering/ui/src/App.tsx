import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Footer } from './Footer/Footer';
import { Hero } from './Hero/Hero';
import { Menu } from './Menu/Menu';
import { Navbar } from './Navbar/Navbar';
import { Orders } from './Orders/Orders';

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
