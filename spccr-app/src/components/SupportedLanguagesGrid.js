import React from "react";
import { Box, Typography } from "@mui/material";

const SupportedLanguagesGrid = ({ gameData }) => {
  const languagesString =
    gameData[Object.keys(gameData)[0]][Object.keys(gameData)[0]]?.data
      ?.supported_languages;

  if (!languagesString) {
    return (
      <Typography variant="h5" textAlign="left">
        No supported languages available
      </Typography>
    );
  }

  const languages = languagesString
    .split(",")
    .map((lang) => lang.replace(/<[^>]*>/g, "").trim());

  return (
    <Box>
      <Typography variant="h4" color="action.main" mb={1}>
        Supported Languages
      </Typography>
      <Box
        sx={{
          display: "flex",
          flexWrap: "wrap",
          gap: 2,
        }}
      >
        {languages.map((language, index) => (
          <Box
            key={index}
            sx={{
              borderRadius: "4px",
              padding: "8px 16px",
              backgroundColor: "background.main",
              border: (theme) => `1px solid ${theme.palette.text.tertiary}`,
              textAlign: "center",
            }}
          >
            <Typography variant="h5" fontSize="1rem">
              {language}
            </Typography>
          </Box>
        ))}
      </Box>
    </Box>
  );
};

export default SupportedLanguagesGrid;
