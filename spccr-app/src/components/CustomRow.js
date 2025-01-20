import { Box, Typography } from "@mui/material";
import CustomIconFrame from "./CustomIconFrame";

function CustomRow({ className, title, description, iconPath, alt, right }) {
  return (
    <Box
      className={className}
      flexDirection={!right ? "row-reverse" : "row"}
      display="flex"
      gap={{ xs: 3, md: 5 }}
      justifyContent="center"
      alignItems="center"
    >
      <CustomIconFrame iconPath={iconPath} alt={alt} />
      <Box
        width={{ xs: "200px", sm: "300px", md: "500px" }}
        textAlign={right ? "right" : "left"}
      >
        {title}
        <Typography variant="body1">{description}</Typography>
      </Box>
    </Box>
  );
}
export default CustomRow;
