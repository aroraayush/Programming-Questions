// https://leetcode.com/problems/add-to-array-form-of-integer/
// OneNote notebook : https://1drv.ms/u/s!Al8jX5-HB-eXgYcEZHkf-_cZZeb8Cg

var a = [2,1,5]
var b = 806;
let c = new Array();
let digit_sum = undefined;
let carry = 0;

a = a.reverse();
b = b.toString().split("").reverse();
var len = Math.max(a.length,b.length)

for (let i=0;i<len;i++){
	if(!a[i])
		a.push(0)
	if(!b[i])
		b.push(0)
	digit_sum = a[i]+ parseInt(b[i]) + carry;
	if(digit_sum>=10){
		let mod = digit_sum % 10;
		carry =  parseInt(digit_sum / 10);
		c.push(mod);
	}
	else{
		carry = 0;
		c.push(digit_sum)
	}
}
if(carry)
	c.push(carry)
console.log("c", c.reverse());

