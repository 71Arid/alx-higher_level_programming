#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  list.forEach(function (item) {
    if (item === searchElement) {
      occ += 1;
    }
  });
  return occ;
};
