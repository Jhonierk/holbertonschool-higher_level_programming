#!/usr/bin/node
exports.converter = function (base) {
  function converterNum (numero) {
    return numero.toString(base);
  }
  return converterNum;
};
