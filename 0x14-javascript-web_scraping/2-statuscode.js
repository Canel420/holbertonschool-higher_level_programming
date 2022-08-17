#!/usr/bin/node

const { error } = require('console');

const axios = require('axios').default;
const URL = process.argv[2];

axios.get(URL)
  .then(function (response) {
    console.log("code: " + response.status);
  })
  .catch(function (err) {
    console.error("code: " + err.response.status);
  });
