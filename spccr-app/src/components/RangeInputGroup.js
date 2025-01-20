import { Box, TextField, Slider, Typography } from "@mui/material";
import { useFormikContext } from "formik";

const RangeInputGroup = ({
  label,
  description,
  minValue,
  maxValue,
  sliderMarks,
  step,
  fieldValues,
  setFieldValue,
  minFieldName,
  maxFieldName,
}) => {
  const { errors, touched } = useFormikContext();

  const hasMinError =
    touched.filtersData?.[minFieldName] && errors.filtersData?.[minFieldName];
  const hasMaxError =
    touched.filtersData?.[maxFieldName] && errors.filtersData?.[maxFieldName];

  return (
    <Box sx={{ marginY: 7 }}>
      <Typography
        variant="h3"
        color="action.main"
        fontSize={{ xs: "2.5rem", sm: "3rem" }}
      >
        {label}
      </Typography>
      <Typography variant="body1" mb={3}>
        {description}
      </Typography>
      <Box
        display="flex"
        alignItems="top"
        justifyContent="space-between"
        sx={{ width: "90%", margin: "0 auto" }}
      >
        <TextField
          label="Minimum value"
          type="number"
          value={fieldValues[minFieldName]}
          onChange={(e) => {
            const value = +e.target.value;
            setFieldValue(
              `filtersData.${minFieldName}`,
              Math.min(value, fieldValues[maxFieldName])
            );
          }}
          inputProps={{ min: minValue, max: maxValue, step }}
          sx={{
            width: { xs: "20%", md: "17%" },
          }}
          error={!!hasMinError}
          helperText={hasMinError ? errors.filtersData[minFieldName] : ""}
        />
        <Slider
          value={[fieldValues[minFieldName], fieldValues[maxFieldName]]}
          onChange={(_, newValue) => {
            setFieldValue(`filtersData.${minFieldName}`, newValue[0]);
            setFieldValue(`filtersData.${maxFieldName}`, newValue[1]);
          }}
          marks={sliderMarks}
          valueLabelDisplay="auto"
          min={minValue}
          max={maxValue}
          step={step}
          sx={{ width: { xs: "40%", md: "55%" } }}
        />
        <TextField
          label="Maximum value"
          type="number"
          value={fieldValues[maxFieldName]}
          onChange={(e) => {
            const value = +e.target.value;
            setFieldValue(
              `filtersData.${maxFieldName}`,
              Math.max(value, fieldValues[minFieldName])
            );
          }}
          inputProps={{ min: minValue, max: maxValue, step }}
          sx={{
            width: { xs: "20%", md: "17%" },
          }}
          error={!!hasMaxError}
          helperText={hasMaxError ? errors.filtersData[maxFieldName] : ""}
        />
      </Box>
    </Box>
  );
};

export default RangeInputGroup;
