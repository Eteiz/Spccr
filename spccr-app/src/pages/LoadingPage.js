import { Container, Box } from "@mui/material";
import { Mosaic } from "react-loading-indicators";

const LoadingPage = () => {
  return (
    <Container>
      <Box
        display="flex"
        alignItems={"center"}
        justifyContent={"center"}
        height="23vh"
        paddingY="27vh"
      >
        <Mosaic
          color="#FCF3FF"
          size="large"
          text="Loading"
          textColor="#FCF3FF"
        />
      </Box>
    </Container>
  );
};
export default LoadingPage;
