<template>
  <div class="card">
    <div class="card-header">
      <h5 class="card-title">Puntajes de entrenamiento</h5>
    </div>
    <div class="card-body">
      <table class="table table-stripped">
        <thead>
          <tr>
            <th scope="col">Precisión</th>
            <th scope="col">Pérdida</th>
          </tr>
        </thead>
        <tbody v-bind:key="vals.index" v-for="vals in values">
          <tr>
            <td>{{ vals.accuracy }}</td>
            <td>{{ vals.loss }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Metrics",
  data() {
    return {
      values: [],
    };
  },
  created() {
    this.loadHistory();
  },
  methods: {
    loadHistory() {
      axios
        .get("http://127.0.0.1:5000/about_model")
        .then((res) => {
          this.values.push(res.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
