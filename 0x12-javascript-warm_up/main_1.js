#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(5, function (nb) {
  console.log('New value: ' + nb);
  addMeMaybe(nb, function (nb2) {
    console.log('New value2: ' + nb2);
    addMeMaybe(nb2, function (nb3) {
      console.log('New value3: ' + nb3);
    });
  });
});
