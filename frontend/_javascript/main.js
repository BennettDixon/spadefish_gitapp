'use strict';

document.addEventListener('DOMContentLoaded', () => {
  console.log('Hello Bulma!');
});

// sample language usage data. 'raw language name': byte_count_integer 
const rawData = {
  'C': 12345,
  'Python': 23456,
  'JavaScript': 5432,
  'Rust': 876
};

// create user-friendly sample array of objects
const sample = Object.keys(rawData).map(k => Object({language: k, bytes: rawData[k]}));
const highestByteCount = Math.max(...sample.map(s => s.bytes));

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
  .domain([0, highestByteCount]);

// create y-axis on the left
chart.append('g')
  .call(d3.axisLeft(yScale));

// define split range into bands and use lang name as band labels
const xScale = d3.scaleBand()
  .range([0, width])
  .domain(sample.map((s) => s.language))
  .padding(0.2);

// create x-axis at the bottom of our chart
chart.append('g')
  .attr('transform', `translate(0, ${height})`)
  .call(d3.axisBottom(xScale));

// start drawing rectangles. TODO add more detailed documentation.
let bars = chart.selectAll().data(sample);

bars.enter().append('rect')
  .attr('x', s => xScale(s.language))
  .attr('y', s => yScale(s.bytes))
  .attr('height', s => height - yScale(s.bytes))
  .attr('width', xScale.bandwidth())
  .attr('fill', '#F8FFD9');