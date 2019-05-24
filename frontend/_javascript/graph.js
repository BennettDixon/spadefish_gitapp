const barChart = () => {
  // sample language usage data. 'name': bytes_of_code => ['name', bytes_of_code]
  let sample = {
    C: 12345,
    Python: 23456,
    JavaScript: 5432,
    Rust: 876,
  };
  sample = Object.keys(sample).map(key => [key, sample[key]]);

  // chart with 1000px width and 600px height, with 80px margin
  const margin = 80;
  const width = 1000 - 2 * margin;
  const height = 600 - 2 * margin;

  // select svg and then pad with margin value to define chart canvas
  const svg = d3.select('div.bar-chart svg');
  const chart = svg.append('g').attr('transform', `translate(${margin}, ${margin})`);

  // define linear scale from 0 to 100 for percentages
  const yScale = d3.scaleLinear()
    .range([height, 0])
    .domain([0, 100]);

  // create y-axis on the left
  chart.append('g')
    .call(d3.axisLeft(yScale));

  // define split range into bands and use lang name as band labels
  const xScale = d3.scaleBand()
    .range([0, width])
    .domain(sample.map(s => s[0]))
    .padding(0.2);

  // create x-axis at the bottom of our chart
  chart.append('g')
    .attr('transform', `translate(0, ${height})`)
    .call(d3.axisBottom(xScale));
};

export default barChart;
