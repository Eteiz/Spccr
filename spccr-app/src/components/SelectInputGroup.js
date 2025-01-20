import React from "react";
import {
  Box,
  Typography,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  FormHelperText,
} from "@mui/material";

const SelectInputGroup = ({
  label,
  description,
  labelNames,
  fieldNames,
  setFieldValue,
  preferencesData,
  options,
  errors,
  touched,
}) => {
  const SYSTEM_OS_MAPPING = {
    0: { start: 0, end: null, step: 1 },
    1: { start: 1, end: 16, step: 2 },
    2: { start: 2, end: null, step: 1 },
    3: { start: 3, end: 16, step: 2 },
    4: { start: 4, end: null, step: 1 },
    5: { start: 5, end: 16, step: 2 },
    6: { start: 6, end: null, step: 1 },
    7: { start: 7, end: 16, step: 2 },
    8: { start: 8, end: null, step: 1 },
    9: { start: 9, end: 16, step: 2 },
    10: { start: 10, end: null, step: 1 },
    11: { start: 11, end: 16, step: 2 },
    12: { start: 12, end: null, step: 1 },
    13: { start: 13, end: 16, step: 2 },
  };

  const handleChange = (fieldName, selectedIndex) => {
    if (["processor", "ram", "graphics", "macOs"].includes(fieldName)) {
      const updatedValues = preferencesData[fieldName].map((_, index) =>
        index >= selectedIndex ? 1 : 0
      );
      setFieldValue(`preferencesData.${fieldName}`, updatedValues);
    } else if (["windowsOs", "linuxOs"].includes(fieldName)) {
      const mapping = SYSTEM_OS_MAPPING[selectedIndex] || {
        start: selectedIndex,
        end: null,
        step: 1,
      };
      const { start, end, step } = mapping;

      const updatedValues = preferencesData[fieldName].map((_, index) => {
        if (
          index >= start &&
          (end === null || index < end) &&
          (index - start) % step === 0
        ) {
          return 1;
        }
        return 0;
      });
      setFieldValue(`preferencesData.${fieldName}`, updatedValues);
    } else {
      setFieldValue(`preferencesData.${fieldName}`, selectedIndex);
    }
  };

  const getSelectedIndex = (fieldName) => {
    const fieldValues = preferencesData[fieldName];
    if (!fieldValues) return "";
    const selectedIndex = fieldValues.findIndex((value) => value === 1);
    return selectedIndex !== -1 ? selectedIndex : "";
  };

  return (
    <Box sx={{ marginY: 7 }}>
      <Typography
        variant="h3"
        color="action.main"
        fontSize={{ xs: "2.5rem", sm: "3rem" }}
      >
        {label}
      </Typography>
      <Typography variant="body1" mb={5} width="90%" marginX="auto">
        {description}
      </Typography>
      <Box
        display="flex"
        alignItems="top"
        flexDirection={{ xs: "column", sm: "row" }}
        justifyContent="space-between"
        sx={{ width: "90%", margin: "0 auto", gap: 2 }}
      >
        {fieldNames.map((fieldName, index) => {
          const isError =
            touched?.preferencesData?.[fieldName] &&
            errors?.preferencesData?.[fieldName];

          const selectedIndex = getSelectedIndex(fieldName);

          return (
            <FormControl
              key={fieldName}
              sx={{ width: { xs: "100%", sm: "32%" } }}
              error={Boolean(isError)}
            >
              <InputLabel id={`${fieldName}-label`}>
                {labelNames[index]}
              </InputLabel>
              <Select
                labelId={`${fieldName}-label`}
                label={labelNames[index]}
                value={selectedIndex}
                onChange={(e) => handleChange(fieldName, e.target.value)}
                MenuProps={{
                  PaperProps: {
                    sx: {
                      backgroundColor: "background.dark",
                      maxHeight: 400,
                    },
                  },
                }}
              >
                {options[index] &&
                  Object.entries(options[index]).map(([key, value, index]) => (
                    <MenuItem key={key} value={key}>
                      {value}
                    </MenuItem>
                  ))}
              </Select>
              {isError && (
                <FormHelperText>
                  {errors.preferencesData[fieldName]}
                </FormHelperText>
              )}
            </FormControl>
          );
        })}
      </Box>
    </Box>
  );
};

export default SelectInputGroup;
