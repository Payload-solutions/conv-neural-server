
<template>
  <div>
    <canvas id="planet-chart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import planetChartData from '../planet-data.js'
import axios from 'axios';


export default {
  name: 'PlanetChart',
  data() {
    return {
      planetChartData: planetChartData,
      valElements: []
    }
  },
  created(){
    this.loadElements();
  },methods:{
    loadElements(){
      axios.get("http://localhost:5000/chart-values")
        .then((res) => {
          this.valElements = res.data;
          console.log(this.valElements);
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  mounted() {
    const ctx = document.getElementById('planet-chart');
    new Chart(ctx, this.planetChartData);
  }
}
</script>