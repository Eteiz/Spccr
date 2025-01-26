import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: {
      main: "#000027",
      transparent: "#000027B3",
    },
    success: {
      main: "#66CC33",
    },
    error: {
      main: "#F44336",
    },
    text: {
      primary: "#FCF3FF",
      secondary: "#D832DA",
      tertiary: "#00A4E7",
      tertiaryHover: "#63BEE3",
      disabled: "#8B8B8B",
    },
    background: {
      main: "#0A0055",
      light: "#2F005D",
      dark: "#000038",
      disabled: "#CFCFCF",
      disabledOutline: "#EEEDED",
    },
    action: {
      main: "#D832DA",
      hover: "#E778E9",
      pressed: "#65008A",
    },
    gradients: {
      primary: "linear-gradient(#000038, #0A0055)",
      secondary: "linear-gradient(#0A0055, #000038)",
      radial: "radial-gradient(circle, #000027, #1C0051, #480092)",
      border: "linear-gradient(45deg, #E778E9, #00A4E7, #2F005D)",
    },
  },
  typography: {
    fontFamily: "'Roboto', sans-serif",
    color: "#FCF3FF",
    button: {
      fontFamily: "'Staatliches', sans-serif",
      fontSize: "2.125rem",
    },
    h1: {
      fontSize: "6rem",
      fontFamily: "'Staatliches', sans-serif",
      color: "#FCF3FF",
    },
    h1r: {
      display: "block",
      fontSize: "6rem",
      fontFamily: "'Rubik One', sans-serif",
      color: "#D832DA",
    },
    h2r: {
      display: "block",
      fontSize: "3.75rem",
      fontFamily: "'Rubik One', sans-serif",
      color: "#D832DA",
    },
    h2: {
      fonySize: "3.75rem",
      fontFamily: "'Staatliches', sans-serif",
      color: "#FCF3FF",
    },
    h3r: {
      fontSize: "3rem",
      fontFamily: "'Rubik One', sans-serif",
      color: "#D832DA",
    },
    h3: {
      fontSize: "3rem",
      fontFamily: "'Staatliches', sans-serif",
      color: "#FCF3FF",
    },
    h4: {
      fontSize: "2.125rem",
      fontFamily: "'Staatliches', sans-serif",
    },
    h5: {
      fontSize: "1.5rem",
      fontFamily: "'Staatliches', sans-serif",
    },
    h6: {
      fontSize: "1.25rem",
      fontFamily: "'Roboto', sans-serif",
      color: "#FCF3FF",
    },
    body1: {
      fontSize: "1rem",
      color: "#FCF3FF",
    },
  },
  shadows: [
    "0px 3px 5px 1px rgba(6, 6, 30, 1)", // default
    "0px 3px 5px 1px rgba(6, 6, 30, 0.55)", // transparent
    "0px 3px 5px 1px rgba(6, 6, 30, 1)",
    "0px 3px 5px 1px rgba(6, 6, 30, 0.55)",
    "0px 3px 5px 1px rgba(6, 6, 30, 1)",
    "0px 3px 5px 1px rgba(6, 6, 30, 0.55)",
    "0px 3px 5px 1px rgba(6, 6, 30, 1)",
    "0px 3px 5px 1px rgba(6, 6, 30, 0.55)",
    "0px 3px 5px 1px rgba(6, 6, 30, 1)",
  ],
  components: {
    MuiTooltip: {
      styleOverrides: {
        tooltip: {
          backgroundColor: "#000038",
        },
      },
    },
    MuiTableCell: {
      styleOverrides: {
        root: {
          fontFamily: "'Staatliches', sans-serif",
          fontSize: "1.5rem",
        },
      },
    },
    MuiCheckbox: {
      styleOverrides: {
        root: {
          "&.Mui-checked": {
            color: "#00A4E7",
          },
          "&:hover": {
            color: "#E778E9",
            backgroundColor: "rgba(0, 0, 255, 0.1)",
          },
          "&.Mui-checked:hover": {
            color: "#63BEE3",
          },
        },
      },
    },
    MuiSelect: {
      styleOverrides: {
        root: {
          borderColor: "#FCF3FF",
          "& .MuiOutlinedInput-notchedOutline": {
            borderColor: "#FCF3FF",
          },
          "&:hover .MuiOutlinedInput-notchedOutline": {
            borderColor: "#E778E9",
          },
          "&.Mui-focused .MuiOutlinedInput-notchedOutline": {
            borderColor: "#65008A",
          },
          "& .MuiSelect-icon": {
            color: "#FCF3FF",
          },
        },
      },
    },
    MuiInputLabel: {
      styleOverrides: {
        root: {
          color: "#D832DA",
          fontFamily: "'Staatliches', sans-serif",
          fontSize: "19px",
          "&.Mui-focused": {
            color: "#D832DA",
          },
        },
      },
    },
    MuiMenuItem: {
      styleOverrides: {
        root: {
          color: "#FCF3FF",
          "&:hover": {
            backgroundColor: "#2F005D",
          },
          "&.Mui-selected": {
            backgroundColor: "#00A4E7",
            "&.Mui-focusVisible": { backgroundColor: "#00A4E7" },
            "&:hover": {
              backgroundColor: "#63BEE3",
            },
          },
        },
      },
    },
    MuiTextField: {
      styleOverrides: {
        root: {
          "& input[type='date']::-webkit-calendar-picker-indicator": {
            filter: "invert(100%) brightness(1.2)",
          },
          "& .MuiOutlinedInput-notchedOutline": {
            borderColor: "#FCF3FF",
          },
          "&:hover .MuiOutlinedInput-notchedOutline": {
            borderColor: "#E778E9",
          },
          "& .MuiOutlinedInput-root.Mui-focused .MuiOutlinedInput-notchedOutline":
            {
              borderColor: "#65008A",
            },
        },
        input: {
          padding: "8px",
        },
      },
    },
    MuiSlider: {
      styleOverrides: {
        root: {
          color: "#FCF3FF",
          "& .MuiSlider-valueLabel": {
            backgroundColor: "#000038",
          },
        },
        mark: {
          backgroundColor: "#FCF3FF",
          height: "8px",
          width: "8px",
          borderRadius: "50%",
        },
        markLabel: {
          fontSize: "1rem",
          color: "#FCF3FF",
        },
        markLabelActive: {
          fontWeight: "bold",
        },
      },
    },
    MuiContainer: {
      styleOverrides: {
        root: {
          maxWidth: "100% !important",
          padding: "0px !important",
        },
      },
    },
    MuiCard: {
      styleOverrides: {
        root: {
          backgroundColor: "#000027B3",
          boxShadow: "0px 3px 5px 1px rgba(6, 6, 30, 0.55)",
        },
      },
    },
    MuiLink: {
      styleOverrides: {
        root: {
          color: "#FCF3FF",
          textDecoration: "none",
          transition: "color 0.3s ease",
          "&:hover": {
            color: "#D832DA",
          },
          "&:active": {
            color: "#65008A",
          },
        },
      },
    },
    MuiButton: {
      styleOverrides: {
        root: {
          width: "260px",
          height: "60px",
        },
      },
      variants: [
        {
          props: { variant: "default" },
          style: ({ theme }) => ({
            backgroundColor: theme.palette.action.main,
            color: theme.palette.text.primary,
            boxShadow: theme.shadows[1],
            "&:hover": {
              backgroundColor: theme.palette.action.hover,
            },
            "&:disabled": {
              backgroundColor: theme.palette.background.disabled,
              color: theme.palette.text.disabled,
            },
            "&:active": {
              backgroundColor: theme.palette.action.pressed,
            },
          }),
        },
        {
          props: { variant: "reversed" },
          style: ({ theme }) => ({
            backgroundColor: theme.palette.text.primary,
            color: theme.palette.action.main,
            boxShadow: theme.shadows[1],
            border: `1px solid ${theme.palette.action.main}`,
            "&:hover": {
              backgroundColor: theme.palette.action.hover,
              color: theme.palette.text.primary,
              border: "none",
            },
            "&:disabled": {
              backgroundColor: theme.palette.background.disabledOutline,
              color: theme.palette.text.disabled,
              border: `1px solid ${theme.palette.text.disabled}`,
            },
            "&:active": {
              backgroundColor: theme.palette.action.pressed,
              color: theme.palette.text.primary,
              border: "none",
            },
          }),
        },
        {
          props: { variant: "outlined" },
          style: ({ theme }) => ({
            backgroundColor: "transparent",
            color: theme.palette.text.primary,
            boxShadow: theme.shadows[1],
            border: `1px solid ${theme.palette.text.primary}`,
            "&:hover": {
              backgroundColor: theme.palette.action.hover,
              color: theme.palette.text.primary,
              border: "none",
            },
            "&:disabled": {
              backgroundColor: theme.palette.background.disabledOutline,
              color: theme.palette.text.disabled,
              border: `1px solid ${theme.palette.text.disabled}`,
            },
            "&:active": {
              backgroundColor: theme.palette.action.pressed,
              color: theme.palette.text.primary,
              border: "none",
            },
          }),
        },
        {
          props: { variant: "outlined" },
          style: ({ theme }) => ({
            backgroundColor: "transparent",
            color: theme.palette.text.primary,
            boxShadow: theme.shadows[1],
            border: `1px solid ${theme.palette.text.primary}`,
            "&:hover": {
              backgroundColor: theme.palette.action.hover,
              color: theme.palette.text.primary,
              border: "none",
            },
            "&:disabled": {
              backgroundColor: theme.palette.background.disabledOutline,
              color: theme.palette.text.disabled,
              border: `1px solid ${theme.palette.text.disabled}`,
            },
            "&:active": {
              backgroundColor: theme.palette.action.pressed,
              color: theme.palette.text.primary,
              border: "none",
            },
          }),
        },
        {
          props: { variant: "borderless" },
          style: ({ theme }) => ({
            backgroundColor: "transparent",
            color: theme.palette.text.primary,
            fontSize: "1.5rem",
            width: "140px",
            height: "40px",
            "&:hover": {
              color: theme.palette.action.hover,
            },
            "&:disabled": {
              color: theme.palette.text.disabled,
            },
            "&:active": {
              color: theme.palette.action.pressed,
            },
          }),
        },
      ],
    },
  },
});
export default theme;
