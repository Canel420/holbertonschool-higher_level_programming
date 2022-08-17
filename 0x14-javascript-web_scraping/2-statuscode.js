#!/usr/bin/node

const axios = require('axios').default;
const URL = process.argv[2];

axios.get(URL)
  .then(function (response) {
    console.log('code: ' + response.status);
  })
  .catch(function (err) {
    console.log('code: ' + err.response.status);
  });
