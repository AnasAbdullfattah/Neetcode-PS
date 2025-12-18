/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    if(nums.length<=2) return nums
    let shuffled_list = []
    let y = n
    for (let x = 0; x < n; x++) {
        shuffled_list.push(nums[x])
        shuffled_list.push(nums[y])
        y++  
    }
    return shuffled_list
};
