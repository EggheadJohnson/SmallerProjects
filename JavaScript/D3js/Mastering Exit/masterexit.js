var numbers = [];
for (x = 0; x < 70; x++){
  numbers.push(Math.floor(10*Math.random())+1);
}

function updateCircles() {
  console.log("updateCircles", numbers);
  var selection = d3.select("svg")
    .selectAll("circle").data(numbers)
    .attr("cx", function(d, i){ return 20+20*(i%10); })
    .attr("cy", function(d, i) { return 20*Math.floor(i/10)+10; })
    .attr("r", function(d) {return d;});
  selection.enter()
    .append("circle")
    .attr("cx", function(d, i){ return 20+20*(i%10); })
    .attr("cy", function(d, i) { return 20*Math.floor(i/10)+10; })
    .attr("r", function(d) {return d;})
    .on("click", function(d, i) {
      numbers.splice(i, 1);
      updateCircles();
    });
  selection.exit().remove();
}



var body = d3.select("body").append("button").text("booga").on("click", function() {
  numbers.push(Math.floor(10*Math.random())+1);
  updateCircles();

});
var running;
function stopAddingCircles(){
  console.log("bluh");
  clearInterval(running);
}

var body = d3.select("body").append("button").text("reset").on("click", function() {
  numbers = [];

  running = setInterval(function(){
        numbers.push(Math.floor(10*Math.random())+1);
        updateCircles();
        if( numbers.length >= 70) {

          stopAddingCircles();}

    }, 14);
});

var body = d3.select("body").append("button").text("sort").on("click", function(){
  numbers.sort(function(a, b){
    if (a > b) return 1;
    else if (a < b) return -1;
    else return 0;
  });
  updateCircles();
});

var body = d3.select("body").append("button").text("shuffle").on("click", function(){
  for (var x = 0; x < numbers.length; x++){
    var swap = Math.floor(Math.random()*numbers.length);
    var temp = numbers[swap];
    numbers[swap] = numbers[x];
    numbers[x] = temp;
  }
  updateCircles();
});

updateCircles();
