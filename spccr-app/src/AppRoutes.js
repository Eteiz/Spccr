import React from "react";
import { Routes, Route } from "react-router-dom";
import { HomePage, AboutPage, ContactPage, NotFoundPage } from "./pages";
import { FormPage, FormResultPage } from "./pages/form";

const AppRoutes = () => {
  return (
    <Routes>
      {/* Main routes */}
      <Route path="/" element={<HomePage />} />
      <Route path="/about" element={<AboutPage />} />
      <Route path="/contact" element={<ContactPage />} />
      <Route path="form/form" element={<FormPage />} />
      <Route path="form/result" element={<FormResultPage />} />
      {/* Not found route */}
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
};

export default AppRoutes;
