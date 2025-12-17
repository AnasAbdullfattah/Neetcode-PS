/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  if (nums.length <= 1) {
    return nums.length;
  }

  let left = 1;
  for (let right = 1; right < nums.length; right++) {
    if (nums[right - 1] !== nums[right]) {
      nums[left] = nums[right];
      left++;
    }
  }
  return left;
};
