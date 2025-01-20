import { AppBar, Box, Toolbar, Typography } from "@mui/material";
import Logo from "./Logo";
import SocialLinksColumn from "./SocialLinksColumn";

function Footer() {
  return (
    <AppBar position="static">
      <Toolbar>
        <Box
          display="flex"
          flexDirection={{ xs: "column", lg: "row" }}
          justifyContent="space-between"
          alignItems="center"
          marginX={2}
          marginY={3}
          gap={{ xs: 2, lg: 0 }}
          sx={{ width: "100%" }}
        >
          <Logo />
          <Typography variant="h5" textAlign="center">
            © Copyright 2025. Made by Marta Ambroziak
          </Typography>
          <SocialLinksColumn />
        </Box>
      </Toolbar>
    </AppBar>
  );
}
export default Footer;
