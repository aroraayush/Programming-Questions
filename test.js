// https://leetcode.com/problems/add-to-array-form-of-integer/

(()=>{
	let a = [1,2,0,0]
	global.b = [3,4]
	// let len = Math.max(a.length,b.length)
	let c = new Array();
	let digit_sum = undefined;
	let carry = 0;
	console.log("b", b);
	for (let i=a.length;i>0;i--){
		console.log("i",i);
		console.log("global.b", global.b);
		let b = global.b[i] ? global.b[i] : 0;
		digit_sum = a[i]+b;
		// if(digit_sum>10){
		// 	let mod = ; digit_sum % 10;
		// 	carry =  parseInt(digit_sum / 10);
		// 	c.push(mod);
		// }
		// else
		c.push(digit_sum)
	}
	console.log("c", c);
})();

