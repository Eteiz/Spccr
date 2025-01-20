import { Box, Typography, Link } from "@mui/material";

function Logo() {
  return (
    <Link href="\">
      <Box display="flex" alignItems="center" gap={2}>
        <Box
          component="img"
          src={`${process.env.PUBLIC_URL}/spccr_icon.png`}
          alt="Logo"
          sx={{
            width: 54,
            height: 54,
          }}
        />
        <Typography variant="h4">SPCCR</Typography>
      </Box>
    </Link>
  );
}
export default Logo;
