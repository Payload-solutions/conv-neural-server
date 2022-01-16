import axios from "axios";

export default {
  name: "fetchStatisticsData",
  props: ["fetchstatisticsdata"],
  data() {
    return {
      accuracy: [],
      loss: [],
      dataLabels:[],
    };
  },
  created() {},
  methods: {
    fetchStatistics() {
      axios.get("http://localhost:5000/chart-values")
        .then((res) => {
          this.accuracy = res.data.message.accuracy;
          this.loss = res.data.message.loss;
          for (let i = 1; i <= this.accuracy.length; i++) {
            this.dataLabels.push(i);
          }
          })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
