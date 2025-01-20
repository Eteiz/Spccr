import React from "react";
import { Box, Typography } from "@mui/material";

const DataGrid = ({ gameData, fieldName }) => {
  const data =
    gameData[Object.keys(gameData)[0]][Object.keys(gameData)[0]]?.data?.[
      fieldName
    ];

  if (!data || data.length === 0) {
    return (
      <Typography variant="h5" textAlign="left">
        No {fieldName} available
      </Typography>
    );
  }

  return (
    <Box>
      <Typography variant="h4" color="action.main" mb={1}>
        {fieldName.charAt(0).toUpperCase() + fieldName.slice(1)}
      </Typography>
      <Box
        sx={{
          display: "flex",
          flexWrap: "wrap",
          gap: 2,
        }}
      >
        {data.map((item, index) => (
          <Box
            key={item.id || index}
            sx={{
              borderRadius: "4px",
              padding: "8px 16px",
              backgroundColor: "background.main",
              border: (theme) => `1px solid ${theme.palette.text.tertiary}`,
              textAlign: "center",
            }}
          >
            <Typography variant="h5" fontSize={"1.25rem"}>
              {item.description || "No description"}
            </Typography>
          </Box>
        ))}
      </Box>
    </Box>
  );
};

export default DataGrid;
