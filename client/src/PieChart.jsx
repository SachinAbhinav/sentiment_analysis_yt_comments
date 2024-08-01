import React from 'react';
import { PieChart, Pie, Cell, Tooltip, Legend } from 'recharts';

// Sample data


function PieChartComponent({d}){
  const {positive, negative, neutral} = d

  const data = [
    { name: 'Positive', value: positive },
    { name: 'Negative', value: negative },
    { name: 'Neutral', value: neutral },
    // { name: 'Group D', value: 200 },
  ];
  
  // Colors for the pie slices
  const COLORS = ['#0088FE', '#00C49F', '#FFBB28'];

  return (
    <PieChart width={400} height={400}>
      <Pie
        data={data}
        dataKey="value"
        nameKey="name"
        outerRadius={150}
        fill="#8884d8"
        label
      >
        {data.map((entry, index) => (
          <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
        ))}
      </Pie>
      <Tooltip />
      <Legend />
    </PieChart>
  );
};

export default PieChartComponent;
