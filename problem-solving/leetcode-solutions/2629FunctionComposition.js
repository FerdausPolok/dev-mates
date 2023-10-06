// Problem: https://leetcode.com/problems/function-composition/

var compose = function(functions) {
    res= 0
	return function(x) {
        for (let i =functions.length-1; i>=0; i--){
            console.log(functions[i](x))
            x = functions[i](x)
        }
        return x
    }
};
