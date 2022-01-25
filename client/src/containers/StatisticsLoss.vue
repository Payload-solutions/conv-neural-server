<template>
  <div>
    <div class="statisticsLoss">
      <canvas id="statistics-loss-data"></canvas>
    </div>
  </div>
</template>

<script>
import Chart from "chart.js";
import StatisticsLoss from "../services/StatisticsLossValues";


export default {
  name: "StatisticsLoss",
  props: ["statisticsLoss"],
  data() {
    return {
      StatisticsLoss:StatisticsLoss,
    };
  },
  mounted() {
    const ctx = document.getElementById("statistics-loss-data");
    new Chart(ctx, this.StatisticsLoss);
  },
};
</script>

<style>
.statisticsLoss {
  padding-top: 50px;
  padding-left: 170px;
  height: 75%;
  width: 80%;
}
</style>
