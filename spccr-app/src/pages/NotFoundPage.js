import { Container, Typography, Button, Box, Link } from "@mui/material";

const NotFoundPage = () => {
  return (
    <Container>
      <Box
        display="flex"
        alignItems={"center"}
        flexDirection={"column"}
        justifyContent={"center"}
        gap={2}
        textAlign={"center"}
        height="23vh"
        paddingY="27vh"
      >
        <Box>
          <Typography
            variant="h2"
            sx={{
              background: (theme) => theme.palette.gradients.border,
              WebkitBackgroundClip: "text",
              WebkitTextFillColor: "transparent",
              fontFamily: "Rubik One",
              fontSize: "9rem",
            }}
          >
            404
          </Typography>
        </Box>
        <Typography variant="h3">Oops! Page not found.</Typography>
        <Typography varian="body1">
          Sorry, the page you're looking for doesn't exist.
        </Typography>
        <Link href="/">
          <Button variant="outlined" sx={{ marginTop: 3 }}>
            Go to main page
          </Button>
        </Link>
      </Box>
    </Container>
  );
};
export default NotFoundPage;
