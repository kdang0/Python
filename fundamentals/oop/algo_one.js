/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

//   const str1 = "aaaabbcddd";
//   const expected1 = "a4b2c1d3";
  
//   const str2 = "";
//   const expected2 = "";
  
//   const str3 = "a";
//   const expected3 = "a";
  
//   const str4 = "bbcc";
//   const expected4 = "bbcc";
  
//   const str5 = "aaaabbcdddaaa";
//   const expected5 = "a7b2c1d3";
//   const expected5_bonus = "a4b2c1d3a3";
  
  
  
  
  /**
   * Encodes the given string such that duplicate characters appear once followed
   * by a number representing how many times the char occurs. Only encode strings
   * when the result yields a shorter length.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str The string to encode.
   * @returns {string} The given string encoded.
   */
  function encodeStr(str) {
    let freq = {}
    let newString = ""
    for(let i = 0; i<str.length; i++){
        if(freq[str[i]]){
            freq[str[i]]++;
        } else{
            freq[str[i]] = 1;
        }
    }
    for(key in freq){
        newString += key;
        newString += freq[key];
    }
    if(newString.length >= str.length){
        newString = str;
    }
    console.log(freq);
    return newString;
  }


//   console.log(encodeStr(str1));
//   console.log(encodeStr(str2));
//   console.log(encodeStr(str3));
//   console.log(encodeStr(str4));
//   console.log(encodeStr(str5));


  /* 
  String Decode  
*/

const str1 = "a3b2c1d3";
const expected1 = "aaabcbddd";

const str2 = "a3b2c12d10";
const expected2 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
 function decodeStr(str) {
    let freq = {};
    let newString = "";
    let numString ="";
    for(let i=0; i< str.length; i++){
        console.log(str[i]);
        if(isNaN(parseInt(str[i+1]))){
            freq[str[i-numString.length]] = parseInt(numString);
            numString = "";
        }
        else{
            numString += str[i];
            if(i === str.length -1 && !isNaN(parseInt(str[i]))){
                console.log(str[i]);
                freq[str[i-numString.length]] = parseInt(numString);
            }
        }
    }
    
    console.log(freq);


    for(property in freq){
        for(let i=0; i < freq[property]; i++){
            newString += property;
            // console.log(newString);
        }
    }
    console.log(`NEW STRING: ${newString}`);
    return newString;
}

console.log(decodeStr(str2));
