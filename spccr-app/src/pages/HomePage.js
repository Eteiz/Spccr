import React, { useEffect } from "react";
import { Container, Box, Typography, Button, Link } from "@mui/material";
import CustomCounterCard from "../components/CustomCounterCard";
import CustomRow from "../components/CustomRow";
import consoleIcon from "../assets/console_icon.png";
import listIcon from "../assets/list_icon.png";
import connectionIcon from "../assets/connection_icon.png";
import backgroundImage from "../assets/background.jpg";
import aiImage from "../assets/ai_image.png";
import examImage from "../assets/exam_image.png";
import gameImage from "../assets/game_image.png";
import rateImage from "../assets/rate_image.png";
import ScrollReveal from "scrollreveal";

const CustomCounterCardData = [
  {
    iconPath: consoleIcon,
    alt: "Console icon",
    title: "1000",
    description: "Games in our database",
  },
  {
    iconPath: listIcon,
    alt: "List icon",
    title: "250",
    description: "Parameter and filter options",
  },
  {
    iconPath: connectionIcon,
    alt: "Connection icon",
    title: "200",
    description: "Neurons in all network's layers",
  },
];
const CustomRowData = [
  {
    title: (
      <Typography
        variant="h3"
        sx={{
          fontSize: { xs: "2.125rem", md: "3rem" },
        }}
      >
        Tell us about{" "}
        <Typography
          component="span"
          variant="h3"
          sx={{
            color: (theme) => theme.palette.action.main,
            fontSize: { xs: "2.125rem", md: "3rem" },
          }}
        >
          your
        </Typography>{" "}
        preferences and gaming setup
      </Typography>
    ),
    description:
      "Share your favorite game types and your gear's specs in a quick, interactive form.",
    iconPath: examImage,
    alt: "Exam icon",
    right: true,
  },
  {
    title: (
      <Typography
        variant="h3"
        sx={{
          fontSize: { xs: "2.125rem", md: "3rem" },
        }}
      >
        Get{" "}
        <Typography
          component="span"
          variant="h3"
          sx={{
            color: (theme) => theme.palette.action.main,
            fontSize: { xs: "2.125rem", md: "3rem" },
          }}
        >
          personalized
        </Typography>{" "}
        game tailored to you
      </Typography>
    ),
    description:
      "Our neural network analyzes your input to match you with the perfect games.",
    iconPath: aiImage,
    alt: "AI icon",
    right: false,
  },
  {
    title: (
      <Typography
        variant="h3"
        sx={{
          fontSize: { xs: "2.125rem", md: "3rem" },
        }}
      >
        Discover your{" "}
        <Typography
          component="span"
          variant="h3"
          sx={{
            color: (theme) => theme.palette.action.main,
            fontSize: { xs: "2.125rem", md: "3rem" },
          }}
        >
          ideal
        </Typography>{" "}
        game with details
      </Typography>
    ),
    description:
      "View the games chosen just for you, complete with detailed insights.",
    iconPath: gameImage,
    alt: "Game icon",
    right: true,
  },
  {
    title: (
      <Typography
        variant="h3"
        sx={{
          fontSize: { xs: "2.125rem", md: "3rem" },
        }}
      >
        Show off your{" "}
        <Typography
          component="span"
          variant="h3"
          sx={{
            color: (theme) => theme.palette.action.main,
            fontSize: { xs: "2.125rem", md: "3rem" },
          }}
        >
          results
        </Typography>{" "}
        to friends
      </Typography>
    ),
    description:
      "Share your personalized picks with friends or send them to your email.",
    iconPath: rateImage,
    alt: "Exam icon",
    right: false,
  },
];

function HomePage() {
  useEffect(() => {
    const sr = ScrollReveal();
    CustomCounterCardData.forEach((_, index) => {
      sr.reveal(`.card-${index}`, {
        origin: "bottom",
        distance: "50px",
        duration: 1000,
        reset: true,
        delay: index * 300,
      });
    });

    ScrollReveal().reveal(".scroll-reveal", {
      distance: "50px",
      origin: "bottom",
      duration: 1000,
      delay: 300,
      reset: true,
    });

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
      {/* Main section */}
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          textAlign: "center",
          height: "100vh",
          gap: 5,
          backgroundImage: `url(${backgroundImage})`,
          backgroundSize: "cover",
          backgroundRepeat: "no-repeat",
          backgroundPosition: "center",
        }}
      >
        <Box
          className="scroll-reveal"
          sx={{
            width: "100%",
          }}
        >
          <Typography variant="h2">Find games for your</Typography>
          <Typography
            variant="h1r"
            sx={{
              fontSize: { xs: "2.75rem", sm: "3.5rem", md: "6rem" },
            }}
          >
            PREFERENCES
          </Typography>
          <Typography variant="h6">
            With our help, you'll never struggle to decide what to play next!
          </Typography>
        </Box>
        <Link href="/form/form">
          <Button variant="default">Get started</Button>
        </Link>
      </Box>
      {/* Card section */}
      <Box
        sx={{
          display: "flex",
          flexDirection: { xs: "column", xl: "row" },
          gap: { xs: 4, xl: 3 },
          justifyContent: "center",
          alignItems: { xs: "center", xl: "flex-start" },
          paddingY: "100px",
          marginX: "0",
          background: (theme) => theme.palette.gradients.primary,
        }}
      >
        <Box
          display="flex"
          gap={2}
          flexDirection="column"
          maxWidth={{ xs: "700px", xl: "276px" }}
          textAlign={{ xs: "center", xl: "left" }}
        >
          <Typography variant="h3">
            Discover the Perfect Game for You!
          </Typography>
          <Typography variant="body1">
            Find games tailored to your preferences and hardware capabilities.
            Our advanced algorithm ensures you get recommendations that suit you
            best.
          </Typography>
        </Box>
        <Box display="flex" gap={3} flexDirection={{ xs: "column", md: "row" }}>
          {CustomCounterCardData.map((card, index) => (
            <CustomCounterCard
              key={index}
              className={`card-${index}`}
              iconPath={card.iconPath}
              alt={card.alt}
              title={card.title}
              description={card.description}
            />
          ))}
        </Box>
      </Box>
      {/* Work section */}
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: 5,
          paddingTop: "50px",
          paddingBottom: "100px",
          background: (theme) => theme.palette.gradients.secondary,
        }}
      >
        <Box textAlign={"center"}>
          <Typography variant="h2">How does</Typography>
          <Typography variant="h1r">SPPCR</Typography>
          <Typography variant="h2">Work?</Typography>
        </Box>
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
        <Link href="/form/form">
          <Button variant="reversed" sx={{ marginTop: 4 }}>
            Get started
          </Button>
        </Link>
      </Box>
    </Container>
  );
}
export default HomePage;
