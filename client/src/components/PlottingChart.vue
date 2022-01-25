<template>
  <div>
    <div class="loss">
      <Statistics />
      <StatisticsLoss/>
    </div>
  </div>
</template>

<script>
import Statistics from '../containers/Statistics.vue'
import StatisticsLoss from "../containers/StatisticsLoss.vue";
export default {
  name: "PlottingChart",
  props: ["plottingChart"],
  components: {
    Statistics,
    StatisticsLoss,
  },
};
</script>
