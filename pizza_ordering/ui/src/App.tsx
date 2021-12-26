import React from 'react';
import { Footer } from './Footer/Footer';
import { Hero } from './Hero/Hero';
import { Menu } from './Menu/Menu';
import { Navbar } from './Navbar/Navbar';

function App() {
  return (
    <div className="App">
      <Navbar />
      <Hero />
      <Menu />
      <Footer />
    </div>
  );
}

export default App;
