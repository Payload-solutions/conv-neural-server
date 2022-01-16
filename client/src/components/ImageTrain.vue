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
            <form @submit.prevent="sendImage">
              <div class="mb-3">
                <label for="formFileSm" class="form-label"
                  >sube una imagen para probar el entrenamiento</label
                >
                <input
                  class="form-control form-control-sm"
                  name="formImageFiles"
                  @change="onChange"
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
      imageData: null,
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
    onChange(event) {
      this.imageData = event.target.files[0];
    },
    sendImage() {
      const formData = new FormData();
      formData.append("formImageFiles", this.imageData, this.imageData.name);
      axios
        .post("http://localhost:5000/train", formData, {
          headers: {
            Accept: "application/json",
            "Content-type": "application/json",
          },
        })
        .then((response) => {
          console.log(response);
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
