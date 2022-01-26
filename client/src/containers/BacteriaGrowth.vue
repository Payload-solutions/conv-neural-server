<template>
  <div class="BacteriaStyle">
    <!-- <h5 class="card-title">Crecimiento bacteriano en 24 horas</h5> -->
    <canvas id="bacteria-vals-data"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js";
import BacteriaMetrics from "../services/BacteriaMetrics.js";
export default {
  name: "BacteriaGrowth",
  data() {
    return {
      BacteriaMetrics: BacteriaMetrics,
    };
  },
  mounted() {
    const ctx = document.getElementById("bacteria-vals-data");
    new Chart(ctx, this.BacteriaMetrics);
  },
  created(){
    this.loadData();
  },
  methods:{
    loadData(){
      setTimeout(this.loadData, 100);
    }
  }
};
</script>

<style>
.BacteriaStyle {
  padding-top: 50px;
  padding-left: 170px;
  padding-bottom: 100px;
  height: 75%;
  width: 80%;
}
</style>
