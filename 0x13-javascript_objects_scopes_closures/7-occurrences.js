#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;

  for (let iter = 0; iter < list.length; iter++) {
    if (list[iter] === searchElement) {
      occurrences++;
    }
  }
  return (occurrences);
};
