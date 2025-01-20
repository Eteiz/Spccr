import React, { useEffect } from "react";
import { Container, Typography, Box } from "@mui/material";
import CustomContactCard from "../components/CustomContactCard";
import ScrollReveal from "scrollreveal";

import { FaGithub, FaLinkedin, FaDiscord } from "react-icons/fa";
import { GrMail } from "react-icons/gr";

const CustomContactCardData = [
  {
    IconComponent: FaGithub,
    alt: "Github icon",
    title: "Github",
    description:
      "Explore the source code of this project and more repositories.",
    href: "https://github.com/Eteiz",
  },
  {
    IconComponent: FaLinkedin,
    alt: "LinkedIn icon",
    title: "LinkedIn",
    description: "Connect with me professionally on LinkedIn.",
    href: "https://www.linkedin.com/in/marta-ambroziak/",
  },
  {
    IconComponent: FaDiscord,
    alt: "Discord icon",
    title: "Discord",
    description: "Join the conversation on Discord and chat with me directly.",
    href: "https://discordapp.com/users/217673306478739458",
  },
  {
    IconComponent: GrMail,
    alt: "Gmail icon",
    title: "E-mail",
    description:
      "Feel free to reach out via email for inquiries or collaborations.",
    href: "mailto:m.ambroziak.contact@gmail.com",
  },
];

function ContactPage() {
  useEffect(() => {
    const sr = ScrollReveal();
    CustomContactCardData.forEach((_, index) => {
      sr.reveal(`.card-${index}`, {
        origin: "bottom",
        distance: "50px",
        duration: 1000,
        reset: true,
        delay: index * 300,
      });
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
        gap={5}
        paddingY={"10vh"}
      >
        <Box textAlign={"center"}>
          <Typography
            variant="h1"
            sx={{
              fontSize: { xs: "4rem", sm: "6rem", md: "6rem" },
            }}
          >
            Contact me
          </Typography>
          <Typography>
            Have any questions? I'd love to hear from you!
          </Typography>
        </Box>
        <Box
          display="grid"
          gridTemplateColumns={{
            xs: "1fr",
            md: "1fr 1fr",
            lg: "1fr 1fr 1fr 1fr",
          }}
          gap={3}
          justifyItems="center"
          alignItems="center"
        >
          {CustomContactCardData.map((card, index) => (
            <CustomContactCard
              key={index}
              className={`card-${index}`}
              IconComponent={card.IconComponent}
              alt={card.alt}
              title={card.title}
              description={card.description}
              href={card.href}
            />
          ))}
        </Box>
      </Box>
    </Container>
  );
}
export default ContactPage;
