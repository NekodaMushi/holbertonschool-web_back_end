function calculateNumber(type, x, y) {
  const operation = {
    SUM: Math.round(x) + Math.round(y),
    SUBTRACT: Math.round(x) - Math.round(y),
    DIVIDE: Math.round(y) === 0 ? "Error" : Math.round(x) / Math.round(y),
  };
  return operation[type] || "Wrong operator chosen";
}

module.exports = calculateNumber;
