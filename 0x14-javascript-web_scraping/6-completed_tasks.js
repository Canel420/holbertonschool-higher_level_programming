#!/usr/bin/node

const axios = require('axios').default;
const URL = process.argv[2];

async function getUserTasks () {
  try {
    const response = await axios.get(URL);
    const data = response.data;
    const tasks = {};
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed) {
        if (data[i].userId in tasks) {
          tasks[data[i].userId]++;
        } else {
          tasks[data[i].userId] = 1;
        }
      }
    }
    console.log(tasks);
  } catch (error) {
    console.error(error);
  }
}

getUserTasks();
