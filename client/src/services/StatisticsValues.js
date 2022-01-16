
import fetchStatisticsData from '../utils/fetchStatisticsData.js';

console.log("fetch", fetchStatisticsData.data().dataLabels);

export const StatisticsValuesData = {
  type: "line",
  data: {
    labels: fetchStatisticsData.data().dataLabels,
    datasets: [
      {
        label: "accuracy",
        data: fetchStatisticsData.data().dataLabels,
        backgroundColor: "rgba(54,73,93,.5)",
        borderColor: "#36495d",
        borderWidth: 3,
      },
      {
        label: "loss",
        data: fetchStatisticsData.data().dataLabels,
        backgroundColor: "rgba(71, 183,132,.5)",
        borderColor: "#47b784",
        borderWidth: 3,
      },
    ],
  },
  options: {
    responsive: true,
    lineTension: 1,
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
            padding: 25,
          },
        },
      ],
    },
  },
};

export default StatisticsValuesData;
