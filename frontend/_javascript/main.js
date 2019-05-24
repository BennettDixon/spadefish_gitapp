'use strict';

document.addEventListener('DOMContentLoaded', () => {
  console.log('Hello Bulma!');
});

// sample language usage data. 'name': bytes_of_code => ['name', bytes_of_code]
const sample = Object.keys({
  'C': 12345,
  'Python': 23456,
  'JavaScript': 5432,
  'Rust': 876
}).map(key => [key, o[key]]);

// chart with 1000px width and 600px height, with 80px margin
const margin = 80;
const width = 1000 - 2 * margin;
const height = 600 - 2 * margin;

// select svg and then pad with margin value to define chart canvas
const svg = d3.select('div.bar-chart svg');
const chart = svg.append('g').attr('transform', `translate(${margin}, ${margin})`);