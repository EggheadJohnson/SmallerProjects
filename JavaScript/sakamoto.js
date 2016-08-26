var dayOfWeek = function(y, m, d) {
	t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4];
	y -= m < 3 ? 1 : 0;
	return (y + Math.floor(y/4) - Math.floor(y/100) + Math.floor(y/400) + t[m-1] + d) % 7;
}

var dayOfWeekName = function(n) {
	return ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][n];
}

console.log(dayOfWeekName(dayOfWeek(1982, 12, 5)));
console.log(dayOfWeekName(dayOfWeek(2016, 5, 4)));
