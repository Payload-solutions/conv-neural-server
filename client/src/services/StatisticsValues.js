import axios from "axios";


let accuracy = [];
let valAccuracy = [];
let loss = [];
let valLoss = [];
let dataFetched = [];
let dataLabels = [];

axios
  .get("http://localhost:5000/history_values")
  .then((res) => {
    dataFetched = res.data.message;
    
    dataFetched.forEach(element => {
      dataLabels.push(element["index"]);
      accuracy.push(element["accuracy"]);
      valAccuracy.push(element["val_accuracy"]);
      loss.push(element["loss"]);
      valLoss.push(element["val_loss"]);
    });

  })
  .catch((error) => {
    console.log(error);
  });

export const StatisticsValuesData = {
  type: "line",
  data: {
    labels: dataLabels,
    datasets: [
      {
        label: "accuracy",
        data: accuracy,
        backgroundColor: "rgba(236, 250, 242, 0.83)",
        borderColor: "#36495d",
        borderWidth: 3,
      },
      {
        label: "valAccuracy",
        data: valAccuracy,
        backgroundColor: "rgba(16, 24, 19, 0.83)",
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
