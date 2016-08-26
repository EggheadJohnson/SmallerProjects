var height,
	width,
	points,
	points2,
	topOfBox,
	traveler,
	arrayOfPoints,
	redraw;

height = 200;
width = 400;
topOfBox = height;

traveler = {
	xCoord: 0,
	yCoord: height,
	forward: function(){
		this.xCoord += width/20;
		if (this.xCoord > width) this.xCoord = width;
		this.yCoord = height-height*Math.sin(Math.PI*this.xCoord/width);
	},
	backward: function(){
		this.xCoord -= width/20;
		if (this.xCoord < 0) this.xCoord = 0;
		this.yCoord = height-height*Math.sin(Math.PI*this.xCoord/width);
	}
}

arrayOfPoints = function(width, height, steps) {
	var result = [0, 0];
	for (var x = 0; x <= steps; x++){
		result.push(x*width/steps);
		result.push(height-height*Math.sin(4*Math.PI*x/width));
	}
	result.push(width);
	result.push(0);
	return result;
}

redraw = function() {
	points = [
			0, height,
			width, height,
			width, topOfBox,
			0, topOfBox
		];
	//console.log(points);
	svg.select("#background").remove();
	svg.select("#hill").remove();
	svg.select("#traveler").remove();
	svg.append("polygon").attr("points", points).attr("style", "fill:purple;stroke:purple;stroke-width:1").attr("id", "background");
	svg.append("polygon").attr("points", points2).attr("style", "fill:white;stroke:black;stroke-width:1;").attr("id", "hill");
	svg.append("circle").attr("cx", traveler.xCoord).attr("cy", traveler.yCoord).attr("r", 3).attr("style", "fill:black;stroke:purple;stroke-width:1").attr("id", "traveler");
}


var body = d3.select("body");
var svg = d3.selectAll("svg");
svg.attr("height", height)
	.attr("width", width);

points = [
			0, height,
			width, height,
			width, height-topOfBox,
			0, height-topOfBox
		];
points2 = arrayOfPoints(width, height, 100);

body.append("br");
body.append("button").text("down")
	.on("click", function(){
		topOfBox += 10;
		if (topOfBox > height) topOfBox = height;
		traveler.backward();
		redraw();
	});
body.append("button").text("up")
	.on("click", function(){
		topOfBox -= 10;
		if (topOfBox > height) topOfBox = height;
		traveler.forward();
		redraw();
	});

redraw();
