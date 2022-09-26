/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {
    let string = ""
    for(let i = str.length-1; i >= 0; i--){
        string += str[i];
    }
    return string;

}


// function reverseString1(str) {
//     str = str.split('');
//     for(let i = 0; i < str.length/2; i++){
//         let temp = str[i];
//         str[i] = str[str.length-1-i];
//         str[str.length-1-i] = temp;
//     }
//     str = str.join('')
//     return str;

// }


console.log(reverseString(str1));