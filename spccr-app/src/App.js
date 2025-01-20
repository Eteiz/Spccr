import React from "react";
import AppRoutes from "./AppRoutes";
import { BrowserRouter as Router } from "react-router-dom";
import { ThemeProvider } from "@emotion/react";
import theme from "./theme/theme";
import NavBar from "./components/NavBar";
import Footer from "./components/Footer";

function App() {
  return (
    <ThemeProvider theme={theme}>
      <NavBar />
      <Router>
        <AppRoutes />
      </Router>
      <Footer />
    </ThemeProvider>
  );
}

export default App;
