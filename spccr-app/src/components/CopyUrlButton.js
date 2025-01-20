import React from "react";
import { Button, Tooltip } from "@mui/material";
import ContentCopyIcon from "@mui/icons-material/ContentCopy";

const CopyUrlButton = () => {
  const handleCopyUrl = () => {
    const currentUrl = window.location.href;
    navigator.clipboard
      .writeText(currentUrl)
      .then(() => {
        alert("URL copied to clipboard!");
      })
      .catch((err) => {
        console.error("Failed to copy URL: ", err);
        alert("Failed to copy URL.");
      });
  };

  return (
    <Tooltip title="Copy URL to clipboard">
      <Button
        variant="reversed"
        onClick={handleCopyUrl}
        endIcon={
          <ContentCopyIcon
            style={{
              fontSize: "32px",
            }}
          />
        }
      >
        Copy URL
      </Button>
    </Tooltip>
  );
};

export default CopyUrlButton;
