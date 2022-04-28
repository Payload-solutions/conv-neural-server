import axios from "axios";


let accuracy = [];
let valAccuracy = [];
let loss = [];
let valLoss = [];
let dataFetched = [];
let dataLabels = [];

axios
  .get("http://143.244.160.173:5000/history_values")
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
        label: "Precisión",
        data: accuracy,
        backgroundColor: "rgba(236, 250, 242, 0.83)",
        borderColor: "#36495d",
        borderWidth: 3,
      },
      {
        label: "Validación de precisión",
        data: valAccuracy,
        backgroundColor: "rgba(236, 250, 242, 0.83)",
        borderColor: "#f4a94d",
        borderWidth: 3,
      }
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
