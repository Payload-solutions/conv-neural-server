<template>
  <div class="image-train">
    <div class="row">
      <div class="col-md-1"></div>
      <div class="col-md-5">
        <div class="card">
          <div class="card-header">
            <h5 class="card-title">Prueba de convolución</h5>
          </div>
          <div class="card-body">
            <form>
              <div class="mb-3">
                <label for="formFileSm" class="form-label"
                  >sube una imagen para probar el entrenamiento</label
                >
                <input
                  class="form-control form-control-sm"
                  id="formFileSm"
                  type="file"
                />
              </div>
              <button type="submit" class="btn btn-outline-secondary">
                <img src="../assets/arrow.png" alt="" /> probar
              </button>
            </form>
          </div>
        </div>
      </div>
      <div class="col-md-5">
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
                  <!-- <th scope="col">Dioxide</th>
                  <th scope="col">Radiation</th> -->
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
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Statistic",
  props: ["statistic"],
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
        .get("http://127.0.0.1:5000/about-model")
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

<style>
.image-train {
  padding-top: 30px;
  margin-right: 30px;
}
</style>
