import { Box } from "@mui/material";

function CustomIconFrame({ iconPath, alt }) {
  return (
    <Box
      sx={{
        position: "relative",
        width: { xs: "100px", sm: "150px", md: "250px" },
        height: { xs: "100px", sm: "150px", md: "250px" },
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        background: (theme) => theme.palette.gradients.radial,
        border: (theme) => `6px solid ${theme.palette.action.hover}`,
        borderRadius: "50%",
      }}
    >
      <Box
        component="img"
        src={iconPath}
        alt={alt}
        sx={{
          width: { xs: "50px", sm: "100px", md: "150px" },
          height: { xs: "50px", sm: "100px", md: "150px" },
          objectFit: "cover",
        }}
      />
    </Box>
  );
}
export default CustomIconFrame;
