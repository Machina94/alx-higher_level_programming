#!/usr/bin/node
const mydict = require('./101-data').dict;
const newDict = {};

for (const k in mydict) {
  if (!(mydict[k] in newDict)) {
    newDict[mydict[k]] = [k];
  } else {
    newDict[mydict[k]].push(k);
  }
}

console.log(newDict);
