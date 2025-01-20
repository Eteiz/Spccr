import { Box } from "@mui/material";
import { FaGithub, FaLinkedin, FaDiscord } from "react-icons/fa";

function SocialLink({ href, children }) {
  return (
    <Box
      component="a"
      href={href}
      target="_blank"
      rel="noopener noreferrer"
      sx={{
        fontSize: "32px",
        color: "#00A4E7",
        transition: "color 0.3s ease",
        "&:hover": {
          color: "#63BEE3",
        },
      }}
    >
      {children}
    </Box>
  );
}

function SocialLinksColumn() {
  return (
    <Box display="flex" gap={2}>
      <SocialLink href={"https://github.com/Eteiz"}>
        <FaGithub />
      </SocialLink>
      <SocialLink href={"https://www.linkedin.com/in/marta-ambroziak/"}>
        <FaLinkedin />
      </SocialLink>
      <SocialLink href={"https://discordapp.com/users/217673306478739458"}>
        <FaDiscord />
      </SocialLink>
    </Box>
  );
}

export default SocialLinksColumn;
