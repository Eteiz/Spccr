import React from "react";
import {
  Typography,
  Box,
  FormGroup,
  FormControlLabel,
  Checkbox,
  Grid,
  Alert,
  Button,
} from "@mui/material";
import { ErrorMessage } from "formik";

const CheckboxGroup = ({
  label,
  description,
  fieldName,
  preferencesData,
  setFieldValue,
  options,
}) => {
  const handleCheckboxChange = (index) => {
    const updatedValues = [...preferencesData[fieldName]];
    updatedValues[index] = updatedValues[index] === 1 ? 0 : 1;
    setFieldValue(`preferencesData.${fieldName}`, updatedValues);
  };

  const handleSelectAll = () => {
    const updatedValues = Object.keys(options).map(() => 1);
    setFieldValue(`preferencesData.${fieldName}`, updatedValues);
  };

  const handleUnselectAll = () => {
    const updatedValues = Object.keys(options).map(() => 0);
    setFieldValue(`preferencesData.${fieldName}`, updatedValues);
  };

  return (
    <Box
      sx={{
        width: "90%",
        marginY: 7,
        marginX: "auto",
      }}
    >
      <Typography
        variant="h3"
        color="action.main"
        fontSize={{ xs: "2.5rem", sm: "3rem" }}
      >
        {label}
      </Typography>
      <Typography variant="body1" mb={3} width="90%" marginX="auto">
        {description}
      </Typography>
      <Box sx={{ display: "flex", justifyContent: "center", mb: 4, gap: 2 }}>
        <Button
          variant="outlined"
          onClick={handleSelectAll}
          sx={{ height: "50px", fontSize: "1.5rem" }}
        >
          Select All
        </Button>
        <Button
          variant="outlined"
          onClick={handleUnselectAll}
          sx={{ height: "50px", fontSize: "1.5rem" }}
        >
          Unselect All
        </Button>
      </Box>
      <FormGroup>
        <Grid
          container
          spacing={2}
          sx={{
            display: "grid",
            gridTemplateColumns: {
              xs: "repeat(1, 1fr)",
              sm: "repeat(2, 1fr)",
              md: "repeat(3, 1fr)",
              lg: "repeat(4, 1fr)",
              xl: "repeat(5, 1fr)",
            },
            gap: 1,
            justifyContent: "center",
            margin: "0 auto",
            width: "100%",
          }}
        >
          {Object.entries(options).map(([key, label], index) => (
            <FormControlLabel
              key={key}
              control={
                <Checkbox
                  checked={preferencesData[fieldName][index] === 1}
                  onChange={() => handleCheckboxChange(index)}
                />
              }
              label={label}
              sx={{ textAlign: "left" }}
            />
          ))}
        </Grid>
      </FormGroup>
      <Box sx={{ mt: 2 }}>
        <ErrorMessage name={`preferencesData.${fieldName}`}>
          {(msg) => (
            <Alert variant="filled" severity="error">
              {msg}
            </Alert>
          )}
        </ErrorMessage>
      </Box>
    </Box>
  );
};

export default CheckboxGroup;
