<template>
    <div class="statistics">
        <canvas id="statistics-vals-data"></canvas>
    </div>
</template>

<script>
    import Chart from 'chart.js';
    import StatisticsValuesData from '../services/StatisticsValues.js';

    export default{
    name: "Statistics",
    props:["statistics"],
    data(){
        return {
            StatisticsValuesData:StatisticsValuesData
        }
    },
    mounted(){
        const ctx = document.getElementById('statistics-vals-data');
        new Chart(ctx, this.StatisticsValuesData);
    }
}
</script>
