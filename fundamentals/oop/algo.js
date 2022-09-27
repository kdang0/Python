/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */
function join(arr, separator) {

}



/* 
Book Index
Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums
span a consecutive range.
*/

// const nums1 = [1, 13, 14, 15, 37, 38, 70];
// const expected1 = "1, 13-15, 37-38, 70";

// const nums2 = [5, 6, 7, 8, 9];
// const expected2 = "5-9";

// const nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
// const expected3 = "1-3, 7, 9, 15-17";

// const nums4 = [1,2,3,4,5,6,7,8,9,10];
// const expected4 = "1-10";

/**
 * Turns the given arr of page numbers into a string of comma hyphenated
 * page ranges.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Page numbers.
 * @returns {string} The given page numbers as comma separated hyphenated
 *    page ranges.
 */

/*
[1, 13, 14, 15, 37, 38, 70];

*/
function bookIndex(nums) {
    let aString = "";
    for(let i=0; i<nums.length; i++){
        let difference = nums[i+1] - nums[i];
        let counter = 1;
        if(i === nums.length-1){
            aString += nums[i];
        }
        else if(difference === 1){
            aString += nums[i] + "-";
            while((i+counter) < nums.length){
                difference = nums[i+counter+1] - nums[i+counter];
                if(difference !== 1){
                    break;
                }
                counter++;
            }
            i += counter;
            if(i === nums.length-1){
                aString += nums[i];
            } else{
                aString += nums[i] + ", ";
            }
        } else{
            aString += nums[i] + ", "
        }
    }
    return aString;
}

console.log(bookIndex([1, 13, 14, 15, 37, 38, 70]));
console.log(bookIndex([5, 6, 7, 8, 9]));
console.log(bookIndex([1,2,3,4,5,6,7,8,9,10]));
console.log(bookIndex([1, 2, 3, 7, 9, 15, 16, 17]));