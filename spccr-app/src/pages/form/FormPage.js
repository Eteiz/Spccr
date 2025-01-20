import React, { useEffect, useState } from "react";
import {
  Container,
  Typography,
  Box,
  Card,
  Button,
  IconButton,
  Alert,
} from "@mui/material";
import ArrowUpwardIcon from "@mui/icons-material/ArrowUpward";
import { Formik, Form } from "formik";
import * as Yup from "yup";
import axios from "axios";
import LoadingPage from "../LoadingPage";
import ErrorPage from "../ErrorPage";
import backgroundImage from "../../assets/background.jpg";
import DateInputGroup from "../../components/DateInputGroup";
import RangeInputGroup from "../../components/RangeInputGroup";
import CheckboxGroup from "../../components/CheckboxGroup";
import SelectInputGroup from "../../components/SelectInputGroup";
import { useNavigate } from "react-router-dom";

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;
const STORAGE_KEY = process.env.STORAGE_KEY;

const FormPage = () => {
  const navigate = useNavigate();
  const [initialValues, setInitialValues] = useState(null);
  const [valueRanges, setValueRanges] = useState(null);
  const [validationSchema, setValidationSchema] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [dictionaries, setDictionaries] = useState({});
  const [resultMessage, setResultMessage] = useState(null);

  const [showScrollToTop, setShowScrollToTop] = useState(false);

  const parseDictionary = (dict) => {
    return Object.fromEntries(
      Object.entries(dict).map(([_, value], index) => [index, value])
    );
  };

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

  const handleSubmit = async (values) => {
    var response = null;
    setResultMessage(null);
    sessionStorage.setItem(STORAGE_KEY, JSON.stringify(values));

    try {
      setLoading(true);
      response = await axios.put(`${API_BASE_URL}/game/predict`, values);
    } catch (err) {
      console.error("Error during prediction:", err);
      setError(err);
    } finally {
      setLoading(false);

      if (response?.data) {
        const { best_match, additional_matches } = response.data;

        if (!best_match && additional_matches.length < 3) {
          setResultMessage(
            "No games found. Please try expanding your filters and preferences."
          );
          return;
        }

        const queryParams = new URLSearchParams({
          resultGame: best_match.game_id,
          resultSimilarity: best_match.similarity_percentage,
          additional1: additional_matches[0]?.[0] || "",
          similarity1: additional_matches[0]?.[1] || "",
          additional2: additional_matches[1]?.[0] || "",
          similarity2: additional_matches[1]?.[1] || "",
          additional3: additional_matches[2]?.[0] || "",
          similarity3: additional_matches[2]?.[1] || "",
        }).toString();

        navigate(`/form/result?${queryParams}`);
      }
    }
  };

  useEffect(() => {
    const storedData = sessionStorage.getItem(STORAGE_KEY);
    let parsedData = storedData ? JSON.parse(storedData) : null;

    const fetchData = async () => {
      try {
        const endpoints = [
          { key: "filters", url: "/dict/filters" },
          { key: "languagesDict", url: "/dict/languages" },
          { key: "categoriesDict", url: "/dict/categories" },
          { key: "genresDict", url: "/dict/genres" },
          { key: "windowsDict", url: "/dict/windows" },
          { key: "linuxDict", url: "/dict/linux" },
          { key: "macDict", url: "/dict/mac" },
          { key: "processorDict", url: "/dict/processor" },
          { key: "memoryDict", url: "/dict/memory" },
          { key: "graphicsDict", url: "/dict/graphics" },
        ];

        const requests = endpoints.map(({ url }) =>
          axios.get(`${API_BASE_URL}${url}`)
        );
        const responses = await Promise.all(requests);

        const data = endpoints.reduce((acc, { key }, index) => {
          acc[key] = responses[index].data;
          return acc;
        }, {});

        const filters = data.filters;
        const ranges = {
          age: [0, filters.maxRequiredAge],
          price: [0, filters.maxPrice],
          releaseDate: [filters.minReleaseDate, filters.maxReleaseDate],
        };
        setValueRanges(ranges);

        if (!parsedData) {
          const defaultData = {
            filtersData: {
              minRequiredAge: 0,
              maxRequiredAge: filters.maxRequiredAge,
              minPrice: 0,
              maxPrice: filters.maxPrice,
              minReleaseDate: filters.minReleaseDate,
              maxReleaseDate: filters.maxReleaseDate,
            },
            preferencesData: {
              supportedLanguages: Array(
                filters.preferenceDataSizes.supportedLanguages
              ).fill(0),
              categories: Array(filters.preferenceDataSizes.categories).fill(0),
              genres: Array(filters.preferenceDataSizes.genres).fill(0),
              windowsOs: Array(filters.preferenceDataSizes.windowsOs).fill(0),
              macOs: Array(filters.preferenceDataSizes.macOs).fill(0),
              linuxOs: Array(filters.preferenceDataSizes.linuxOs).fill(0),
              processor: Array(filters.preferenceDataSizes.processor).fill(0),
              graphics: Array(filters.preferenceDataSizes.graphics).fill(0),
              ram: Array(filters.preferenceDataSizes.ram).fill(0),
            },
          };
          parsedData = defaultData;
        }

        setInitialValues(parsedData);
        setDictionaries({
          languagesDict: parseDictionary(data.languagesDict),
          categoriesDict: parseDictionary(data.categoriesDict),
          genresDict: parseDictionary(data.genresDict),
          windowsDict: parseDictionary(data.windowsDict),
          linuxDict: parseDictionary(data.linuxDict),
          macDict: parseDictionary(data.macDict),
          processorDict: parseDictionary(data.processorDict),
          memoryDict: parseDictionary(data.memoryDict),
          graphicsDict: parseDictionary(data.graphicsDict),
        });

        const schema = createValidationSchema(ranges);
        setValidationSchema(schema);
      } catch (err) {
        console.error("Failed to fetch data:", err);
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const createValidationSchema = (ranges) =>
    Yup.object().shape({
      filtersData: Yup.object().shape({
        minRequiredAge: Yup.number()
          .min(
            ranges.age[0],
            `Minimum required age must be at least ${ranges.age[0]}`
          )
          .max(
            ranges.age[1],
            `Minimum required age must be at most ${ranges.age[1]}`
          )
          .integer("Minimum required age must be an integer")
          .test(
            "min-less-than-max",
            "Minimum required age must be less than maximum required age",
            function (value) {
              const { maxRequiredAge } = this.parent;
              return value <= maxRequiredAge;
            }
          ),
        maxRequiredAge: Yup.number()
          .min(
            ranges.age[0],
            `Maximum required age must be at least ${ranges.age[0]}`
          )
          .max(
            ranges.age[1],
            `Maximum required age must be at most ${ranges.age[1]}`
          )
          .integer("Maximum required age must be an integer"),
        minPrice: Yup.number()
          .min(
            ranges.price[0],
            `Minimum price must be at least ${ranges.price[0]}`
          )
          .max(
            ranges.price[1],
            `Minimum price must be at most ${ranges.price[1]}`
          )
          .test(
            "min-less-than-max",
            "Minimum price must be less than maximum",
            function (value) {
              const { maxPrice } = this.parent;
              return value <= maxPrice;
            }
          ),
        maxPrice: Yup.number()
          .min(
            ranges.price[0],
            `Maximum price must be at least ${ranges.price[0]}`
          )
          .max(
            ranges.price[1],
            `Maximum price must be at most ${ranges.price[1]}`
          ),
        minReleaseDate: Yup.date()
          .min(
            ranges.releaseDate[0],
            `Minimum relese date cannot be earlier than ${ranges.releaseDate[0]}`
          )
          .max(
            ranges.releaseDate[1],
            `Minimum relese date cannot be later than ${ranges.releaseDate[1]}`
          ),
        maxReleaseDate: Yup.date()
          .min(
            ranges.releaseDate[0],
            `Maximum release date cannot be earlier than ${ranges.releaseDate[0]}`
          )
          .max(
            ranges.releaseDate[1],
            `Maximum release date cannot be later than ${ranges.releaseDate[1]}`
          ),
      }),
      preferencesData: Yup.object().shape({
        supportedLanguages: Yup.array()
          .of(Yup.number().oneOf([0, 1]).required("Value must be 0 or 1"))
          .test(
            "at-least-one-selected",
            "At least one supported language must be selected",
            (value) => Array.isArray(value) && value.some((v) => v === 1)
          ),
        categories: Yup.array()
          .of(Yup.number().oneOf([0, 1]).required("Value must be 0 or 1"))
          .test(
            "at-least-one-selected",
            "At least one category must be selected",
            (value) => Array.isArray(value) && value.some((v) => v === 1)
          ),
        genres: Yup.array()
          .of(Yup.number().oneOf([0, 1]).required("Value must be 0 or 1"))
          .test(
            "at-least-one-selected",
            "At least one genre must be selected",
            (value) => Array.isArray(value) && value.some((v) => v === 1)
          ),
        windowsOs: Yup.array()
          .of(Yup.number().oneOf([0, 1]).required("Value must be 0 or 1"))
          .test(
            "at-least-one-selected",
            "Windows Os must be selected",
            (value) => Array.isArray(value) && value.some((v) => v === 1)
          ),
        macOs: Yup.array()
          .of(Yup.number().oneOf([0, 1]).required("Value must be 0 or 1"))
          .test(
            "at-least-one-selected",
            "Mac Os must be selected",
            (value) => Array.isArray(value) && value.some((v) => v === 1)
          ),
        linuxOs: Yup.array()
          .of(Yup.number().oneOf([0, 1]).required("Value must be 0 or 1"))
          .test(
            "at-least-one-selected",
            "Linux Os must be selected",
            (value) => Array.isArray(value) && value.some((v) => v === 1)
          ),
        processor: Yup.array()
          .of(Yup.number().oneOf([0, 1]).required("Value must be 0 or 1"))
          .test(
            "at-least-one-selected",
            "Processor must be selected",
            (value) => Array.isArray(value) && value.some((v) => v === 1)
          ),
        graphics: Yup.array()
          .of(Yup.number().oneOf([0, 1]).required("Value must be 0 or 1"))
          .test(
            "at-least-one-selected",
            "Graphics must be selected",
            (value) => Array.isArray(value) && value.some((v) => v === 1)
          ),
        ram: Yup.array()
          .of(Yup.number().oneOf([0, 1]).required("Value must be 0 or 1"))
          .test(
            "at-least-one-selected",
            "Memory must be selected",
            (value) => Array.isArray(value) && value.some((v) => v === 1)
          ),
      }),
    });

  if (loading) {
    return <LoadingPage />;
  }

  if (error) {
    return <ErrorPage errorText={`Failed to load filters: ${error.message}`} />;
  }

  return (
    <Container
      sx={{
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: "cover",
        paddingBottom: "3vh !important",
      }}
    >
      <Box
        sx={{
          textAlign: "center",
          display: "flex",
          flexDirection: "column",
          paddingTop: "7vh",
          paddingBottom: "5vh",
        }}
      >
        <Typography variant="h2">Fill out your</Typography>
        <Typography
          variant="h1r"
          sx={{ fontSize: { xs: "2.75rem", sm: "3.5rem", md: "6rem" } }}
        >
          GAMING PROFILE
        </Typography>
        <Typography variant="h6">
          Share your preferences to find your perfect game.
        </Typography>
      </Box>
      <Card
        sx={{
          width: { xs: "95%", md: "80%" },
          paddingY: "3vh",
          margin: "auto",
          textAlign: "center",
        }}
      >
        <Formik
          initialValues={initialValues}
          validationSchema={validationSchema}
          onSubmit={handleSubmit}
          enableReinitialize
        >
          {({ values, setFieldValue, errors, touched, isValid }) => {
            return (
              <Form>
                <RangeInputGroup
                  label="Required Age Range"
                  description="The game should be suitable for players minimally between these ages:"
                  minValue={valueRanges.age[0]}
                  maxValue={valueRanges.age[1]}
                  sliderMarks={[
                    {
                      value: valueRanges.age[0],
                      label: `${valueRanges.age[0]}`,
                    },
                    {
                      value: valueRanges.age[1],
                      label: `${valueRanges.age[1]}`,
                    },
                  ]}
                  step={1}
                  fieldValues={values.filtersData}
                  setFieldValue={setFieldValue}
                  minFieldName="minRequiredAge"
                  maxFieldName="maxRequiredAge"
                />
                <DateInputGroup
                  label="Release Date Range"
                  description="The game should have been released between these dates:"
                  minDate={valueRanges.releaseDate[0]}
                  maxDate={valueRanges.releaseDate[1]}
                  fieldValues={values.filtersData}
                  setFieldValue={setFieldValue}
                  minFieldName="minReleaseDate"
                  maxFieldName="maxReleaseDate"
                />
                <RangeInputGroup
                  label="Price Range"
                  description="The game should cost between these amounts in PLN:"
                  minValue={valueRanges.price[0]}
                  maxValue={valueRanges.price[1]}
                  sliderMarks={[
                    {
                      value: valueRanges.price[0],
                      label: `${valueRanges.price[0]}`,
                    },
                    {
                      value: valueRanges.price[1],
                      label: `${valueRanges.price[1]}`,
                    },
                  ]}
                  step={0.01}
                  fieldValues={values.filtersData}
                  setFieldValue={setFieldValue}
                  minFieldName="minPrice"
                  maxFieldName="maxPrice"
                />
                <CheckboxGroup
                  label="Supported Languages"
                  description="The game should be available in these languages:"
                  fieldName="supportedLanguages"
                  preferencesData={values.preferencesData}
                  setFieldValue={setFieldValue}
                  options={dictionaries.languagesDict}
                />
                <CheckboxGroup
                  label="Categories"
                  description="The game should be of categories:"
                  fieldName="categories"
                  preferencesData={values.preferencesData}
                  setFieldValue={setFieldValue}
                  options={dictionaries.categoriesDict}
                />
                <CheckboxGroup
                  label="Genres"
                  description="The game should be of genres:"
                  fieldName="genres"
                  preferencesData={values.preferencesData}
                  setFieldValue={setFieldValue}
                  options={dictionaries.genresDict}
                />
                <SelectInputGroup
                  label="Operational Systems"
                  description="The game should be available on these operating systems:"
                  labelNames={[
                    "Windows operating system",
                    "Mac operating system",
                    "Linux operating system",
                  ]}
                  fieldNames={["windowsOs", "macOs", "linuxOs"]}
                  setFieldValue={setFieldValue}
                  preferencesData={values.preferencesData}
                  options={[
                    dictionaries.windowsDict,
                    dictionaries.macDict,
                    dictionaries.linuxDict,
                  ]}
                  errors={errors}
                  touched={touched}
                />
                <SelectInputGroup
                  label="Gear Parameters"
                  description="The game should require at least these gear parameters:"
                  labelNames={["Procesor", "Graphics", "Memory"]}
                  fieldNames={["processor", "graphics", "ram"]}
                  setFieldValue={setFieldValue}
                  preferencesData={values.preferencesData}
                  options={[
                    dictionaries.processorDict,
                    dictionaries.graphicsDict,
                    dictionaries.memoryDict,
                  ]}
                  errors={errors}
                  touched={touched}
                />
                {resultMessage && (
                  <Box mb={2} width="90%" marginX="auto">
                    <Alert variant="filled" severity="warning">
                      {resultMessage}
                    </Alert>
                  </Box>
                )}
                {!isValid && (
                  <Box mb={2} width="90%" marginX="auto">
                    <Alert variant="filled" severity="error">
                      Please correct the errors above before submitting.
                    </Alert>
                  </Box>
                )}
                <Button variant="default" type="submit">
                  Submit
                </Button>
              </Form>
            );
          }}
        </Formik>
      </Card>
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

export default FormPage;
