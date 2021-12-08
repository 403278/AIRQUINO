<script>

// set the dimensions and margins of the graph
var margin = {top: 80, right: 10, bottom: 30, left: 40},
  width = 450 - margin.left - margin.right,
  height = 450 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#my_dataviz")
.append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
.append("g")
  .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

//Read the data
d3.csv("https://raw.githubusercontent.com/403278/airqino-d3heatmap-test/main/TQ5-07-12-2021-consistant-data.csv", function(data) {

  // Labels of row and columns -> unique identifier of the column called 'group' and 'variable'
  var myTime = d3.map(data, function(d){return d.Time;}).keys()
  var myZone = d3.map(data, function(d){return d.Zone;}).keys()


  // Build X scales and axis:
  var x = d3.scaleBand()
    .range([ 0, width ])
    .domain(myTime)
    .padding(0.005);
  svg.append("g")
    .style("font-size", 2)
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x).tickSize(10))
    .select(".domain").remove()

  // Build Y scales and axis:
  var y = d3.scaleBand()
    .range([ height, 0 ])
    .domain(myZone)
    .padding(0.05);
  svg.append("g")
    .style("font-size", 15)
    .call(d3.axisLeft(y).tickSize(0))
    .select(".domain").remove()

  // Build color scale
  var myColor = d3.scaleSequential()
    .interpolator(d3.interpolateRdYlGn)
    .domain([800,400])

  // create a tooltip
  var tooltip = d3.select("#my_dataviz")
    .append("div")
    .style("opacity", 0)
    .attr("class", "tooltip")
    .style("background-color", "white")
    .style("border", "solid")
    .style("border-width", "2px")
    .style("border-radius", "5px")
    .style("padding", "5px")

  // Three function that change the tooltip when user hover / move / leave a cell
  var mouseover = function(d) {
    tooltip
      .style("opacity", 1)
    d3.select(this)
      .style("stroke", "black")
      .style("opacity", 1)
  }
  var mousemove = function(d) {
    tooltip
      .html("CO2 Level<br>measured: " + d.PPM +" PPM")
      .style("left", (d3.mouse(this)[0]+70) + "px")
      .style("top", (d3.mouse(this)[1]) + "px")
  }
  var mouseleave = function(d) {
    tooltip
      .style("opacity", 0)
    d3.select(this)
      .style("stroke", "none")
      .style("opacity", 0.8)
  }

  // add the squares
  svg.selectAll()
    .data(data, function(d) {return d.Time+':'+d.Zone;})
    .enter()
    .append("rect")
      .attr("x", function(d) { return x(d.Time) })
      .attr("y", function(d) { return y(d.Zone) })
      .attr("rx", 4)
      .attr("ry", 4)
      .attr("width", x.bandwidth() )
      .attr("height", y.bandwidth() )
      .style("fill", function(d) { return myColor(d.PPM)} )
      .style("stroke-width", 4)
      .style("stroke", "none")
      .style("opacity", 0.8)
    .on("mouseover", mouseover)
    .on("mousemove", mousemove)
    .on("mouseleave", mouseleave)
})

// Add title to graph
svg.append("text")
        .attr("x", 0)
        .attr("y", -50)
        .attr("text-anchor", "left")
        .style("font-size", "22px")
        .text("Indoor Air Quality Live");

// Add subtitle to graph
svg.append("text")
        .attr("x", 0)
        .attr("y", -20)
        .attr("text-anchor", "left")
        .style("font-size", "14px")
        .style("fill", "grey")
        .style("max-width", 400)
        .text("D3heatmap indicading when and where CO2 level are Good, Moderate, Unhealthy.");


</script>