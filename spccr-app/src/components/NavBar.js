import React, { useState } from "react";
import {
  AppBar,
  Box,
  Toolbar,
  Button,
  Link,
  Accordion,
  AccordionSummary,
  AccordionDetails,
} from "@mui/material";
import Logo from "./Logo";
import MenuIcon from "@mui/icons-material/Menu";
import CloseIcon from "@mui/icons-material/Close";

const pages = [
  {
    name: "Contact",
    url: "/contact",
  },
  {
    name: "About",
    url: "/about",
  },
];

function NavBar() {
  const [isOpen, setIsOpen] = useState(false);

  const handleAccordionToggle = (_, expanded) => {
    setIsOpen(expanded);
  };

  return (
    <AppBar position="sticky">
      <Toolbar>
        <Box
          display={{ xs: "none", lg: "flex" }}
          flexDirection="row"
          justifyContent="space-between"
          alignItems="center"
          marginX="16px"
          sx={{
            width: "100%",
            height: "88px",
          }}
        >
          <Logo />
          <Box
            display="flex"
            justifyContent="space-between"
            alignItems="center"
          >
            <Box display="flex">
              {pages.map((page) => (
                <Link key={page.name} href={page.url}>
                  <Button variant="borderless">{page.name}</Button>
                </Link>
              ))}
            </Box>
            <Link href="/form/form">
              <Button variant="outlined" sx={{ height: "50px" }}>
                Get started
              </Button>
            </Link>
          </Box>
        </Box>
        <Accordion
          expanded={isOpen}
          onChange={handleAccordionToggle}
          sx={{
            display: { xs: "flex", lg: "none" },
            flexDirection: "column",
            width: "100%",
            backgroundColor: "primary.main",
            boxShadow: "none",
            "&:hover": {
              boxShadow: "none",
            },
            "&:focus-visible": {
              boxShadow: "none",
            },
          }}
        >
          <AccordionSummary
            expandIcon={
              isOpen ? (
                <CloseIcon sx={{ fontSize: "40px", color: "text.primary" }} />
              ) : (
                <MenuIcon sx={{ fontSize: "40px", color: "text.primary" }} />
              )
            }
          >
            <Logo />
          </AccordionSummary>
          <AccordionDetails>
            <Box
              display="flex"
              justifyContent="center"
              flexDirection={{ xs: "column", sm: "row" }}
              alignItems="center"
              gap={3}
            >
              <Box display="flex">
                {pages.map((page) => (
                  <Link key={page.name} href={page.url}>
                    <Button variant="borderless">{page.name}</Button>
                  </Link>
                ))}
              </Box>
              <Link href="/form/form">
                <Button variant="outlined" sx={{ height: "50px" }}>
                  Get started
                </Button>
              </Link>
            </Box>
          </AccordionDetails>
        </Accordion>
      </Toolbar>
    </AppBar>
  );
}
export default NavBar;
