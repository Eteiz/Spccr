import { Box, Typography, Card, CardContent, CardMedia } from "@mui/material";
import CountUp from "react-countup";

function CustomCounterCard({ className, iconPath, alt, title, description }) {
  return (
    <Card
      className={className}
      sx={{
        width: 276,
        height: 276,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "primary.transparent",
      }}
    >
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          width: 80,
          height: 80,
        }}
      >
        <CardMedia
          component="img"
          image={iconPath}
          alt={alt}
          sx={{
            width: 80,
            height: 80,
          }}
        />
      </Box>
      <CardContent sx={{ textAlign: "center" }}>
        <Typography variant="h3r">
          <CountUp start={0} end={title} duration={3} separator="," />+
        </Typography>
        <Typography variant="body1">{description}</Typography>
      </CardContent>
    </Card>
  );
}
export default CustomCounterCard;
