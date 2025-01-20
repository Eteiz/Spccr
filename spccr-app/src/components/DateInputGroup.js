import { Box, Typography, TextField } from "@mui/material";
import { useFormikContext } from "formik";

const DateInputGroup = ({
  label,
  description,
  minDate,
  maxDate,
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
      <Typography variant="body1" mb={3} width="90%" marginX="auto">
        {description}
      </Typography>
      <Box
        display="flex"
        alignItems="top"
        justifyContent="space-between"
        sx={{ width: { xs: "90%", md: "50%" }, margin: "0 auto" }}
      >
        <TextField
          label="From"
          type="date"
          value={fieldValues[minFieldName]}
          onChange={(e) =>
            setFieldValue(`filtersData.${minFieldName}`, e.target.value)
          }
          inputProps={{ min: minDate, max: maxDate }}
          sx={{
            width: "49%",
          }}
          error={!!hasMinError}
          helperText={hasMinError ? errors.filtersData[minFieldName] : ""}
        />
        <TextField
          label="To"
          type="date"
          value={fieldValues[maxFieldName]}
          onChange={(e) =>
            setFieldValue(`filtersData.${maxFieldName}`, e.target.value)
          }
          inputProps={{ min: minDate, max: maxDate }}
          sx={{
            width: "49%",
          }}
          error={!!hasMaxError}
          helperText={hasMaxError ? errors.filtersData[maxFieldName] : ""}
        />
      </Box>
    </Box>
  );
};
export default DateInputGroup;
