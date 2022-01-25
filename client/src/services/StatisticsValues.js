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
        label: "Precisión",
        data: accuracy,
        backgroundColor: "rgba(236, 250, 242, 0.83)",
        borderColor: "#36495d",
        borderWidth: 2,
      },
      {
        label: "Validación de precisión",
        data: valAccuracy,
        backgroundColor: "rgba(236, 250, 242, 0.83)",
        borderColor: "#f4a94d",
        borderWidth: 2,
      }
    ],
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Chart.js Line Chart'
      }
    },
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

// export const StatisticsLoss = {
//   type: "line",
//   data: {
//     labels: dataLabels,
//     datasets: [
//       {
//         label: "Pérdida",
//         data: loss,
//         backgroundColor: "rgba(236, 250, 242, 0.83)",
//         borderColor: "#9aa2c7",
//         borderWidth: 2,
//       },{
//         label: "Validación de pérdida",
//         data: valLoss,
//         backgroundColor: "rgba(236, 250, 242, 0.83)",
//         borderColor: "#47b784",
//         borderWidth: 2,
//       },


//     ],
//   },
//   options: {
//     responsive: true,
//     plugins: {
//       legend: {
//         position: 'top',
//       },
//       title: {
//         display: true,
//         text: 'Chart.js Line Chart'
//       }
//     },
//     lineTension: 2,
//     scales: {
//       yAxes: [
//         {
//           ticks: {
//             beginAtZero: true,
//             padding: 40,
//           },
//         },
//       ],
//     },
//   },
// }

export default StatisticsValuesData;
