import {
  Box,
  Typography,
  Card,
  CardContent,
  Link,
  CardActionArea,
} from "@mui/material";

function CustomContactCard({
  className,
  IconComponent,
  alt,
  title,
  description,
  href,
}) {
  return (
    <Link href={href} target="_blank">
      <Card
        className={className}
        sx={{
          width: 276,
          height: 276,
          backgroundColor: "primary.transparent",
        }}
      >
        <CardActionArea sx={{ width: "100%", height: "100%" }}>
          <Box
            sx={{
              display: "flex",
              justifyContent: "center",
              height: 60,
              fontSize: "3.75rem",
              color: (theme) => theme.palette.text.tertiary,
            }}
          >
            <IconComponent aria-label={alt} />
          </Box>
          <CardContent sx={{ textAlign: "center" }}>
            <Typography variant="h3r">{title}</Typography>
            <Typography variant="body1">{description}</Typography>
          </CardContent>
        </CardActionArea>
      </Card>
    </Link>
  );
}

export default CustomContactCard;
