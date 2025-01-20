import React from "react";
import { Card, Table, TableRow, TableCell, Typography } from "@mui/material";

const RequirementsTable = ({ mainGameData }) => {
  const parseRequirement = (requirement, field) => {
    const regex = new RegExp(`<strong>${field}:</strong>(.*?)<br>`, "i");
    const match = requirement?.match(regex);
    return match ? match[1].trim() : "N/A";
  };

  const renderRequirementRow = (osName, requirements) => {
    const { minimum } = requirements || {};

    return (
      <>
        <TableRow>
          <TableCell sx={{ color: "text.tertiary", pl: 0 }}>
            {osName} Minimum
          </TableCell>
          <TableCell align="right" sx={{ pr: 0 }}>
            <Typography>
              <strong>OS:</strong> {parseRequirement(minimum, "OS")}
            </Typography>
            <Typography>
              <strong>Processor:</strong>{" "}
              {parseRequirement(minimum, "Processor")}
            </Typography>
            <Typography>
              <strong>Memory:</strong> {parseRequirement(minimum, "Memory")}
            </Typography>
            <Typography>
              <strong>Graphics:</strong> {parseRequirement(minimum, "Graphics")}
            </Typography>
          </TableCell>
        </TableRow>
      </>
    );
  };

  return (
    <Card>
      <Typography variant="h4" color="action.main">
        System and Gear Requirements
      </Typography>
      <Table sx={{ width: "98%", margin: "auto" }}>
        {renderRequirementRow("Windows OS", mainGameData?.pc_requirements)}
        {renderRequirementRow("Mac OS", mainGameData?.mac_requirements)}
        {renderRequirementRow("Linux OS", mainGameData?.linux_requirements)}
      </Table>
    </Card>
  );
};

export default RequirementsTable;
