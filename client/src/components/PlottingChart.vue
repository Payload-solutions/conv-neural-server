<template>
  <div>
    <div class="loss">
      <h5 id="title-description" class="card-title">Histórico de entrenamientos</h5>
      <Statistics  />
      <StatisticsLoss />
      <!-- <PlanetChart /> -->
      <h5 id="title-description" class="card-title">Crecimiento bacteriano en 24 horas</h5>
      <BacteriaGrowth/>
    </div>
  </div>
</template>

<script>
import Statistics from './Statistics.vue'
import StatisticsLoss from "./StatisticsLoss.vue";
//import PlanetChart from './PlanetChart.vue';
import BacteriaGrowth from "../containers/BacteriaGrowth.vue"
export default {
  name: "PlottingChart",
  props: ["plottingChart"],
  components: {
    Statistics,
    StatisticsLoss,
    //PlanetChart,
    BacteriaGrowth,
  },
};
</script>

<style>
  #title-description{
    padding-top: 20px;
  }
</style>
