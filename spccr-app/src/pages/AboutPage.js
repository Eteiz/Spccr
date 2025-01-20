import React, { useEffect } from "react";
import ScrollReveal from "scrollreveal";
import { Container, Typography, Box } from "@mui/material";
import aiImage from "../assets/ai_image.png";
import codeImage from "../assets/code_icon.png";
import webImage from "../assets/web_icon.png";
import CustomRow from "../components/CustomRow";

const CustomRowData = [
  {
    title: (
      <Typography
        variant="h3"
        sx={{
          color: (theme) => theme.palette.action.main,
          fontSize: { xs: "2.125rem", md: "3rem" },
        }}
      >
        This is SPCCR
      </Typography>
    ),
    description:
      "SPCCR is a cutting-edge web platform designed to help gamers discover their ideal games based on personal preferences and hardware specifications. Whether you're unsure if a game will run smoothly on your current setup or you're looking for personalized recommendations, SPCCR simplifies the decision-making process by providing accurate and insightful suggestions tailored to you.",
    iconPath: webImage,
    alt: "Web icon",
    right: true,
  },
  {
    title: (
      <Typography
        variant="h3"
        sx={{
          color: (theme) => theme.palette.action.main,
          fontSize: { xs: "2.125rem", md: "3rem" },
        }}
      >
        Intelligent game recommendations
      </Typography>
    ),
    description:
      "At the core of SPCCR lies a powerful backend powered by a neural network, built using Python, PyTorch, and Flask. This intelligent system analyzes gaming preferences, hardware specifications, and extensive data sourced from the Steam API to match players with the best games for their needs. Advanced filters further refine the search, ensuring gamers receive recommendations that align with both their interests and gear capabilities. Detailed game information and insights are also provided to enhance the user experience.",
    iconPath: aiImage,
    alt: "Neural network image",
    right: false,
  },
  {
    title: (
      <Typography
        variant="h3"
        sx={{
          color: (theme) => theme.palette.action.main,
          fontSize: { xs: "2.125rem", md: "3rem" },
        }}
      >
        A modern frontend experience
      </Typography>
    ),
    description:
      "The frontend of SPCCR is crafted with React and Material-UI, delivering a sleek, user-friendly interface. The interactive form, built using Formik and YUP, allows users to seamlessly input their preferences and gear details. Axios ensures efficient and reliable communication between the frontend and backend, enabling fast and responsive recommendations. Every aspect of SPCCR is designed to make finding your next favorite game effortless and enjoyable.",
    iconPath: codeImage,
    alt: "Code icon",
    right: true,
  },
];

function AboutPage() {
  useEffect(() => {
    const sr = ScrollReveal();
    sr.reveal(".scroll-reveal-row", {
      origin: "bottom",
      distance: "50px",
      duration: 1000,
      reset: true,
      interval: 300,
    });
    return () => sr.destroy();
  }, []);

  return (
    <Container>
      <Box
        display="flex"
        flexDirection="column"
        justifyContent={"center"}
        alignItems={"center"}
        gap={10}
        paddingY="10vh"
      >
        <Box textAlign={"center"} maxWidth="90%" width={"1000px"}>
          <Typography
            variant="h1"
            sx={{
              fontSize: { xs: "4rem", sm: "6rem", md: "6rem" },
            }}
          >
            About Site
          </Typography>
          <Typography variant="body1">
            What is SPCCR and how does it work?
          </Typography>
        </Box>
        <Box display="flex" flexDirection="column" gap={10}>
          {CustomRowData.map((row, index) => (
            <CustomRow
              key={index}
              className="scroll-reveal-row"
              title={row.title}
              description={row.description}
              iconPath={row.iconPath}
              alt={row.alt}
              right={row.right}
            />
          ))}
        </Box>
      </Box>
    </Container>
  );
}
export default AboutPage;
