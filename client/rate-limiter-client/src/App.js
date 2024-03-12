import React, { useState, useEffect } from "react";
import "./App.css";

const App = () => {
  const [sentRequests, setSentRequests] = useState(0);
  const [acceptedRequests, setAcceptedRequests] = useState(0);
  const [blockedRequests, setBlockedRequests] = useState(0);

  const apiUrl = "http://127.0.0.1:5000";

  const endpoints = [
    { name: "RequestOrderInvoices", method: "GET" },
    { name: "GetOrderInformation", method: "GET" },
    { name: "CreateOrder", method: "POST" },
  ];

  const makeRequest = async (endpoint) => {
    try {
      const requestOptions = {
        method: endpoint.method,
        headers:
          endpoint.method === "POST"
            ? { "Content-Type": "application/json" }
            : {},
      };

      const response = await fetch(
        `${apiUrl}/${endpoint.name}`,
        requestOptions
      );

      if (response.ok) {
        setAcceptedRequests((prev) => prev + 1);
      } else {
        setBlockedRequests((prev) => prev + 1);
      }
    } catch (error) {
      console.error("Error making request:", error);
    } finally {
      setSentRequests((prev) => prev + 1);
    }
  };

  useEffect(() => {
    const intervalId = setInterval(() => {
      const randomEndpoint =
        endpoints[Math.floor(Math.random() * endpoints.length)];
      makeRequest(randomEndpoint);
    }, 1000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div>
      <h1>Sent Requests: {sentRequests}</h1>
      <h1>Accepted Requests: {acceptedRequests}</h1>
      <h1>Blocked Requests: {blockedRequests}</h1>
    </div>
  );
};

export default App;
