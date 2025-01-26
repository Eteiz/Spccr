import React, { useEffect, useState, useRef } from "react";
import axios from "axios";
import { useLocation } from "react-router-dom";
import {
  Container,
  Box,
  Typography,
  Button,
  Card,
  Table,
  TableBody,
  TableCell,
  TableRow,
  IconButton,
  Link,
} from "@mui/material";
import ArrowUpwardIcon from "@mui/icons-material/ArrowUpward";
import ErrorPage from "../ErrorPage";
import LoadingPage from "../LoadingPage";
import DataGrid from "../../components/DataGrid";
import placeholderImage from "../../assets/placeholder-image.jpg";
import SupportedLanguagesGrid from "../../components/SupportedLanguagesGrid";
import backgroundImage from "../../assets/background.jpg";
import ArrowDownwardIcon from "@mui/icons-material/ArrowDownward";
import RequirementsTable from "../../components/RequirementsTable";
import CopyUrlButton from "../../components/CopyUrlButton";
import ScrollReveal from "scrollreveal";

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

const FormResultPage = () => {
  const location = useLocation();
  const [gameData, setGameData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showScrollToTop, setShowScrollToTop] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > window.innerHeight / 2) {
        setShowScrollToTop(true);
      } else {
        setShowScrollToTop(false);
      }
    };

    window.addEventListener("scroll", handleScroll);
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const gameDetailsRef = useRef(null);

  const scrollToDetails = () => {
    if (gameDetailsRef.current) {
      gameDetailsRef.current.scrollIntoView({ behavior: "smooth" });
    }
  };

  const queryParams = new URLSearchParams(location.search);
  const params = {
    resultGame: queryParams.get("resultGame"),
    resultSimilarity: queryParams.get("resultSimilarity"),
    additional: [
      {
        id: queryParams.get("additional1"),
        similarity: queryParams.get("similarity1"),
      },
      {
        id: queryParams.get("additional2"),
        similarity: queryParams.get("similarity2"),
      },
      {
        id: queryParams.get("additional3"),
        similarity: queryParams.get("similarity3"),
      },
    ],
  };

  useEffect(() => {
    if (!params.resultGame || params.additional.some((item) => !item.id)) {
      setError("Required parameters are missing or incorrect.");
      return;
    }

    const fetchGameData = async () => {
      try {
        const appIds = [
          params.resultGame,
          ...params.additional.map((item) => item.id),
        ].join(",");
        const response = await axios.get(`${API_BASE_URL}/steam/game-details`, {
          params: { appids: appIds },
        });
        setGameData(response.data);
      } catch (err) {
        setError("Failed to load game data.");
      } finally {
        setLoading(false);
      }
    };

    fetchGameData();
  }, []);

  if (loading) return <LoadingPage />;
  if (error) return <ErrorPage errorText={error} />;

  const mainGameData =
    gameData[Object.keys(gameData)[0]][Object.keys(gameData)[0]]?.data;

  const renderTableRows = () => [
    { label: "Required Age", value: mainGameData?.required_age || "0" },
    {
      label: "Developer",
      value: mainGameData?.developers?.join(", ") || "N/A",
    },
    {
      label: "Publisher",
      value: mainGameData?.publishers?.join(", ") || "N/A",
    },
    {
      label: "Price",
      value: mainGameData?.is_free
        ? "Free"
        : mainGameData?.price_overview?.final_formatted || "N/A",
    },
    {
      label: "Release Date",
      value: mainGameData?.release_date?.coming_soon
        ? "Coming Soon"
        : mainGameData?.release_date?.date || "N/A",
    },
  ];

  return (
    <Container>
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          backgroundImage: `url(${backgroundImage})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
          minHeight: "100vh",
          paddingY: { xs: "2.5vh", md: "0vh" },
          width: "100%",
        }}
      >
        <Typography
          variant="h2"
          textAlign={"center"}
          width={{ xs: "90%", md: "50%" }}
        >
          The game chosen for you is
        </Typography>
        <Typography
          variant="h1r"
          textAlign={"center"}
          width="90%"
          fontSize={{ xs: "3.75rem", md: "6rem" }}
        >
          {(mainGameData?.name || "GAME TITLE").toUpperCase()}
        </Typography>
        <Typography variant="h3">Compatibility:</Typography>
        <Typography variant="h3" color="success.main">
          {parseFloat(Number(params.resultSimilarity).toFixed(2))}%
        </Typography>
        <Box
          display="flex"
          flexDirection={{ xs: "column", md: "row" }}
          justifyContent="center"
          gap={2}
          my={3}
          width="80%"
        >
          <Link>
            <CopyUrlButton />
          </Link>
          <Link>
            <Button
              variant="default"
              endIcon={
                <ArrowDownwardIcon
                  style={{
                    fontSize: "32px",
                  }}
                />
              }
              sx={{ width: "100%" }}
              onClick={scrollToDetails}
            >
              Game Details
            </Button>
          </Link>
        </Box>
      </Box>
      {/* Main Game Section */}
      <Box
        sx={{
          background: (theme) => theme.palette.gradients.primary,
          paddingBottom: 5,
          paddingTop: 10,
        }}
      >
        <Typography
          variant="h1r"
          textAlign={{ xs: "center", lg: "left" }}
          width="90%"
          mx="auto"
          fontSize={{ xs: "3.75rem", lg: "6rem" }}
        >
          {(mainGameData?.name || "GAME TITLE").toUpperCase()}
        </Typography>
        <Typography
          variant="h2"
          textAlign={{ xs: "center", lg: "left" }}
          mb={5}
          width="90%"
          mx="auto"
        >
          And Details About It
        </Typography>
        <Box
          display="flex"
          width="90%"
          mx="auto"
          alignItems="flex-start"
          gap={4}
          flexDirection={{ xs: "column", lg: "row" }}
        >
          <Card
            sx={{ width: { xs: "100% - 16px", lg: "400px" }, mx: "auto", p: 2 }}
          >
            <Box
              sx={{
                width: "100%",
                height: "200px",
                mb: 2,
                borderRadius: "4px",
                border: (theme) => `2px solid ${theme.palette.action.pressed}`,
              }}
            >
              <img
                src={mainGameData?.header_image || placeholderImage}
                alt={`${mainGameData?.name || "Game"} Thumbnail`}
                style={{ width: "100%", height: "100%", objectFit: "cover" }}
              />
            </Box>
            <Typography variant="body1" mb={3}>
              {mainGameData?.short_description || "No description available"}
            </Typography>
            <RequirementsTable mainGameData={mainGameData} />
          </Card>
          <Card
            sx={{
              p: 2,
              flex: 1,
              gap: 3,
              display: "flex",
              flexDirection: "column",
            }}
            ref={gameDetailsRef}
          >
            <Table>
              <Typography variant="h4" color="action.main">
                Main Information
              </Typography>
              <TableBody>
                {renderTableRows().map((row, index) => (
                  <TableRow key={index}>
                    <TableCell sx={{ color: "text.tertiary", pl: 0 }}>
                      {row.label}
                    </TableCell>
                    <TableCell align="right" sx={{ pr: 0 }}>
                      <Typography>{row.value}</Typography>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
            <SupportedLanguagesGrid gameData={gameData} />
            <DataGrid gameData={gameData} fieldName="categories" />
            <DataGrid gameData={gameData} fieldName="genres" />
            <Box
              display="flex"
              gap={2}
              flexDirection={{ xs: "column", md: "row" }}
            >
              <Link
                href={`https://store.steampowered.com/app/${mainGameData?.steam_appid}`}
                target="_blank"
                underline="none"
              >
                <Button
                  variant="reversed"
                  sx={{ height: "50px", width: "100%" }}
                >
                  Steam Store Page
                </Button>
              </Link>
              <Link
                href={`https://steamdb.info/app/${mainGameData?.steam_appid}/`}
                target="_blank"
                underline="none"
              >
                <Button
                  variant="outlined"
                  sx={{ height: "50px", width: "100%" }}
                >
                  SteamDB Page
                </Button>
              </Link>
            </Box>
          </Card>
        </Box>
      </Box>
      <Box
        sx={{
          background: (theme) => theme.palette.gradients.secondary,
          paddingBottom: 10,
          paddingTop: 5,
        }}
      >
        <Typography
          variant="h1r"
          textAlign={{ xs: "center", lg: "right" }}
          width="90%"
          mx="auto"
          fontSize={{ xs: "3.75rem", lg: "6rem" }}
        >
          OTHER GAMES
        </Typography>
        <Typography
          variant="h2"
          textAlign={{ xs: "center", lg: "right" }}
          mb={5}
          width="90%"
          mx="auto"
        >
          You may also check and like
        </Typography>
        <Box
          display="flex"
          justifyContent="center"
          gap={3}
          flexWrap="wrap"
          width="90%"
          mx="auto"
        >
          {params.additional.map((item, index) => {
            const additionalGameData =
              gameData[Object.keys(gameData)[index + 1]]?.[
                Object.keys(gameData)[index + 1]
              ]?.data;

            if (!additionalGameData) return null;

            return (
              <Card
                key={item.id}
                sx={{ width: { xs: "90%", md: "45%", lg: "29%" }, p: 2 }}
              >
                <Box>
                  <Typography variant="h3" color="action.main">
                    {additionalGameData?.name || "Game Title"}
                  </Typography>
                  <Box
                    sx={{
                      width: "100%",
                      height: "200px",
                      my: 2,
                      borderRadius: "4px",
                      border: (theme) =>
                        `2px solid ${theme.palette.action.pressed}`,
                      overflow: "hidden",
                    }}
                  >
                    <img
                      src={additionalGameData?.header_image ?? placeholderImage}
                      alt={`${additionalGameData?.name || "Game"} Thumbnail`}
                      style={{
                        width: "100%",
                        height: "100%",
                        objectFit: "cover",
                      }}
                    />
                  </Box>
                  <Typography variant="body1" mb={2} minHeight="150px">
                    {additionalGameData?.short_description ||
                      "No description available"}
                  </Typography>
                </Box>
                <Box
                  display="flex"
                  justifyContent="space-between"
                  width="100%"
                  mt={2}
                >
                  <Typography variant="h4" color="action.main">
                    Compatibility
                  </Typography>
                  <Typography variant="h4" color="success.main">
                    {item.similarity
                      ? `${parseFloat(item.similarity).toFixed(2)}%`
                      : "N/A"}
                  </Typography>
                </Box>
                <Link
                  href={`https://store.steampowered.com/app/${item.id}`}
                  target="_blank"
                  underline="none"
                >
                  <Button
                    variant="outlined"
                    sx={{ mt: 2, width: "100%", height: "50px" }}
                  >
                    Steam Store Page
                  </Button>
                </Link>
              </Card>
            );
          })}
        </Box>
      </Box>
      {showScrollToTop && (
        <IconButton
          onClick={scrollToTop}
          sx={{
            position: "fixed",
            bottom: "4rem",
            right: "3rem",
            zIndex: 1000,
            backgroundColor: "primary.main",
            color: "text.primary",
            "&:hover": {
              backgroundColor: "background.main",
            },
          }}
        >
          <ArrowUpwardIcon fontSize="large" />
        </IconButton>
      )}
    </Container>
  );
};

export default FormResultPage;
