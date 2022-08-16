#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter((currentElm) => currentElm === searchElement).length;
};
