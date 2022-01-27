//import axios from "axios";

let bacteriaArray = [
  3.62, 3.53, 3.69, 3.69, 3.63, 3.97, 4.26, 4.26, 4.14, 4.3, 4.13, 4.13, 5.23,
  5.37, 4.9, 4.9, 6.27, 6.41, 7.22, 7.22, 7.57, 7.66, 7.36, 7.36, 8.38, 8.19,
  8.33, 8.33, 8.7, 8.69, 7.9, 7.9, 8.62, 8.41, 8.56, 8.56, 8.44, 8.23, 8.51,
  8.51,
];
let timeArray = [
  0, 0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4, 6, 6, 6, 6, 8, 8, 8, 8, 10, 10, 10, 10,
  12, 12, 12, 12, 16, 16, 16, 16, 20, 20, 20, 20, 24, 24, 24, 24,
];

export const BacteriaMetrics = {
  type: "line",
  data: {
    labels: timeArray,
    datasets: [
      {
        label: "Crecimiento bacteriano",
        data: bacteriaArray,
        backgroundColor: "rgba(54,73,93,.5)",
          borderColor: "#36495d",
        borderWidth: 3,
      },
    ],
  },
  options: {
    responsive: true,
    lineTension: 2,
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
            padding: 40,
          },
        },
      ],
    },
  },
};

export default BacteriaMetrics;
