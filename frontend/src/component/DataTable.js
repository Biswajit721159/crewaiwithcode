import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useLocation } from 'react-router-dom';
import { Table } from 'react-bootstrap';

function DataTable(props) {

  const location = useLocation();
  const { data } = location?.state;

  return (
    <Table striped bordered hover>
      <thead>
        <tr>
          {data?.length > 0 && Object.keys(data?.[0]).map((key) => (
            <th key={key}>{key}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data?.map((item, index) => (
          <tr key={index}>
            {Object?.values(item)?.map((value, i) => (
              <td key={i}>{value}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </Table>
  );
}

export default DataTable;