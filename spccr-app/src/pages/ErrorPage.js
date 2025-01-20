import { Container, Typography, Button, Box, Link } from "@mui/material";

const ErrorPage = ({ errorText }) => {
  return (
    <Container>
      <Box
        display="flex"
        flexDirection={"column"}
        justifyContent={"center"}
        gap={1}
        alignItems={"center"}
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
              fontSize: { xs: "5.5rem", md: "9rem" },
            }}
          >
            ERROR
          </Typography>
        </Box>
        <Typography varian="body1" width="90%">
          {errorText}
        </Typography>
        <Link href="/">
          <Button variant="outlined" sx={{ marginTop: 4 }}>
            Go to main page
          </Button>
        </Link>
      </Box>
    </Container>
  );
};
export default ErrorPage;
