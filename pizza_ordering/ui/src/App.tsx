import { createContext, useState } from "react";
import { Route, Routes } from "react-router-dom";
import { Footer } from "./components/Footer/Footer";
import { Menu } from "./components/Menu/Menu";
import { Navbar } from "./components/Navbar/Navbar";
import { Orders } from "./components/Orders/Orders";

type AppContextType = {
  flashMessage: string;
  flashMessageStatus: string;
  setFlashMessageStatus: (status: string) => void;
  setFlashMessage: (errorMessage: string) => void;
};

export const AppContext = createContext<AppContextType | null>(null);

function App() {
  const [flashMessage, setFlashMessage] = useState("");
  const [flashMessageStatus, setFlashMessageStatus] = useState("");

  return (
    <AppContext.Provider
      value={{ flashMessage, flashMessageStatus, setFlashMessage, setFlashMessageStatus }}
    >
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<Menu />} />
          <Route path="order" element={<Orders />} />
        </Routes>
        <Footer />
      </div>
    </AppContext.Provider>
  );
}

export default App;
