import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";

import { Context } from "../store/appContext";

export const Family = () => {
  const [result, setResult] = useState({});

  useEffect(() => {
    var requestOptions = {
      method: "GET",
      body: raw,
      redirect: "follow",
    };

    fetch(
      "https://3000-4geeksacade-reactflaskh-0pyiido6m10.ws-eu77.gitpod.io/api/family/",
      requestOptions
    )
      .then((response) => response.json())
      .then((result) => setResult(result))
      .catch((error) => console.log("error", error));
  }, []);

  return (
    <>
      {result.results?.map((element) => {
        return (
          <div className="home text-center m-5" key={element.name}>
            <div>
              <p className="Text text-center">Familia</p>
              <div className="row text-center m-5">{element.name}</div>
              <div className="row text -center m-5">{element.lastname}</div>
              <div className="row text -center m-5">{element.years}</div>
            </div>
          </div>
        );
      })}
    </>
  );
};
