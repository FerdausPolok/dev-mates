// https://leetcode.com/problems/valid-anagram/

var isAnagram = function (s, t) {
    if (s.length != t.length) return false
    if (s.split("").sort().join("") != t.split("").sort().join("")) return false
    else return true
};
