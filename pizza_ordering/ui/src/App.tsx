import React from 'react';
import { Hero } from './Hero/Hero';
import { Menu } from './Menu/Menu';
import { Navbar } from './Navbar/Navbar';

function App() {
  return (
    <div className="App">
      <Navbar />
      <Hero />
      <Menu />
    </div>
  );
}

export default App;
