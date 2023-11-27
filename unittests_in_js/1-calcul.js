function calculateNumber(type, a, b) {
  const operation = {
    SUM: Math.round(a) + Math.round(b),
    SUBTRACT: Math.round(a) - Math.round(b),
    DIVIDE: Math.round(b) === 0 ? "Error" : Math.round(a) / Math.round(b),
  };
  return operation[type] || "Wrong operator chosen";
}

module.exports = calculateNumber;
