/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
  s = s.trim().split(" ");
  let result = s[s.length - 1].length;
  return result;
};
